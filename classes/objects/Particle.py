import sys
from ..tools.Coordinates import Coordinates
from ..tools.physical_constants import gravitational_constant
# from ..tools.gravity import gravity
#https://stackoverflow.com/questions/13851438/how-to-store-a-big-dictionary
import numpy as np
from time import sleep
# from classes.tools.Coordinates import Coordinates
class Particle(Coordinates):
    def __init__(self, label, mass=None, position=[0,0,0], velocity=[0,0,0], type="Cartesian"):
        global gravity
        self.label = label
        self.mass = mass
        self.type = type
        self.velocity = velocity
        gravity={}


        if self.type == "Cartesian":
            print("also cartesian")
            self.position=position
            self.Cartesian(position=position)
        elif self.type == 'Spherical':
            pass
        elif self.type == 'Polar':
            pass
        elif self.type == 'Lorentz':
            pass
    def move(self,time_i,t_step,force=[0,0,0],impulse_frame=[0,0]):
        grav=[0,0,self.G(self.z)]
        self.velocity=[v+0.5*(g+a+f/self.mass)*np.float_power(t_step,2) for v,a,f,g in zip(self.velocity,self.accel,force,grav)]
        self.position=[round(pos+vel*t_step,3) for pos,vel in zip(self.position,self.velocity)]
        BOUNCE=True
        elasticity=0.5
        if self.position[2]<=0 and BOUNCE==True:
            self.position[2]=abs(self.position[2])
            self.velocity[2]=abs(self.velocity[2])*elasticity
        return self.position
    def G(self, altitude):
        global gravity
        altitude=round(altitude/1000)
        m1 = 5.972*(10**24)
        earth = 6.3781*(10**6)
        # gConst = 6.673/(10**11)
        if altitude in gravity.keys():
            return gravity[altitude]
        else:
            print(f"GRAVITY NOT FOUND AT {altitude}km, recalculating!")
            gravity[altitude] = -(gravitational_constant*m1)/(np.power(altitude+6.3781*(10**6),2))
            # print(f"gravity at {altitude}: {gravity[altitude]}")
            return gravity[altitude]
    def initG(self, max_alt):
        global gravity
        gravity = {}
        print("Please wait: Importing Gravity...")
        grav = open("gravity.py","w+")
        grav.write("gravity={\n")
        for altitude in range(max_alt+1):
            grav.write(f"\t\'{altitude}\':[0,0,{round((self.G(1000*altitude)[2]),4)}],\n")
        grav.write("}")
        print("Gravity Imported. Enjoy!")
        grav.close()
        sleep(5)
