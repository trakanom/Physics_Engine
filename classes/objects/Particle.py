import sys
from ..tools.Coordinates import Coordinates
from ..tools.physical_constants import gravitational_constant
# from ..tools.gravity import gravity
#https://stackoverflow.com/questions/13851438/how-to-store-a-big-dictionary
import numpy as np
from time import sleep
# from classes.tools.Coordinates import Coordinates
class Particle(Coordinates):
    def __init__(self, label="Starship", mass=None, position=[0,0,0], velocity=[0,0,0],acceleration=[0,0,0] type="Cartesian",primary_body=None):
        global gravity
        self.label = label
        self.mass = mass
        self.type = type
        self.velocity = velocity
        if primary_body!=None:
            self.primary_body = primary_body
        else:
            try:
                self.primary_body = Earth
            except:
                self.primary_body = None


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
        grav=[0,0,self.primary_body.GravitationalForce(self.z)]
        self.velocity=[v+0.5*(g+a+f/self.mass)*np.float_power(t_step,2) for v,a,f,g in zip(self.velocity,self.accel,force,grav)]
        self.position=[round(pos+vel*t_step,3) for pos,vel in zip(self.position,self.velocity)]
        BOUNCE=True
        elasticity=0.5
        if self.position[2]<=0 and BOUNCE==True:
            self.position[2]=abs(self.position[2])
            self.velocity[2]=abs(self.velocity[2])*elasticity
        return self.position
