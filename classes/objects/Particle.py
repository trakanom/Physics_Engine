import sys
from ..tools.Coordinates import Coordinates
from ..tools.physical_constants import GRAVITATIONAL_CONSTANT
# from ..tools.gravity import gravity
#https://stackoverflow.com/questions/13851438/how-to-store-a-big-dictionary
import numpy as np
from time import sleep
# from classes.tools.Coordinates import Coordinates
class Particle(Coordinates):
    def __init__(self, label="Starship", mass=None, position=None, velocity=None,acceleration=None, type=None,primary_body=None, elasticity=0):
        if position is None:
            position=tuple([0,0,0])
        if velocity is None:
            velocity = tuple([0,0,0])
        if acceleration is None:
            acceleration= tuple([0,0,0])
        if type is None:
            type = "Cartesian"
        super().__init__(type, position)
        self.label = label
        self.mass = mass
        self.type = type
        self.velocity = velocity
        self.acceleration = acceleration
        self.elasticity = elasticity
        if primary_body!=None:
            self.primary_body = primary_body
        else:
            try:
                self.primary_body = Earth
            except:
                self.primary_body = None


        if self.type == "Cartesian":
            # print("also cartesian")
            self.position=position
            # self.Cartesian(position=position)
            self.path = [[] for i in range(1+len(position))]
        elif self.type == 'Spherical':
            pass
        elif self.type == 'Polar':
            pass
        elif self.type == 'Lorentz':
            pass
    def move(self,time_i,t_step,force=None,impulse_frame=None):
        if force==None:
            force = [0,0,0]
            impulse_frame = [0,0]
        myForce = [0,0,65000000] #[x,y,z] Newtons, [t_0,t_f] seconds
        i_frame = [0,6*600] #Will be active from 0 to 3600 seconds.
        force = myForce if i_frame[0]<=time_i<=i_frame[1] else force
        gravity=self.primary_body.GravitationalForce(self.z)
        if self.type=="Cartesian":
            gravity = [0,0,gravity]
        elif self.type=="Spherical" or self.type=="Cylindrical":
            gravity = [gravity,0,0]
        self.velocity=[v+0.5*(g+a+f/self.mass)*np.float_power(t_step,2) for v,a,f,g in zip(self.velocity,self.acceleration,force,gravity)]
        self.position=[round(pos+vel*t_step,3) for pos,vel in zip(self.position,self.velocity)]
        BOUNCE=True
        if self.position[2]<=0 and BOUNCE:
            self.position[2]=abs(self.position[2])
            self.velocity[2]=abs(self.velocity[2])*self.elasticity
        self.x=self.position[0]
        self.y=self.position[1]
        self.z=self.position[2]
        self.path[0].append([time_i])
        self.path[1].append(self.x)
        self.path[2].append(self.y)
        self.path[3].append(self.z)
        return self.position
    def pathing(self,entry="all"):
        if entry=="all":
            # mycoords=(['x','y','z'] if self.type=="Cartesian" else ['rho','theta','phi'])
            # print("t = {0},\t{1}".format(self.path[0],*zip(mycoords,self.path[1:]),sep="\n"))
            return self.path