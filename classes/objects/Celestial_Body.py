import sys
import numpy as np
from ..tools.Coordinates import Coordinates
from ..tools.physical_constants import gravitational_constant
class Celestial_Body(Coordinates):
    def __init__(self,label="Earth",mass=0,radius=0,atmosphere=False):
        self.label = label
        self.mass=mass
        self.radius=radius
        self.gravity={}
        if atmosphere==True:
            self.atmosphere={}
        self.populateConstants(1000)
    def populateConstants(self,entries):
        for i in range(entries):
            # print(f"Dicts populating...\t{round(100*i/entries)}% ({i}/{entries}).")
            i=1000*i
            self.GravitationalForce(i)
            if self.atmosphere!=True:
                self.AtmosphericDensity(i)
        # print(*zip(self.gravity.keys(),self.gravity.values(),self.atmosphere.values()), sep="\n")
    def GravitationalForce(self,altitude):

        altitude=1000*round(altitude/1000,0)
        # gConst = 6.673/(10**11)
        if altitude in self.gravity.keys():
            return self.gravity[altitude]
        else:
            # print(f"GRAVITY NOT FOUND AT {altitude}km, recalculating!")
            self.gravity[altitude] = -(gravitational_constant*self.mass)/(np.power(altitude+self.radius,2))
            # print(f"gravity at {altitude}: {gravity[altitude]}")
            return self.gravity[altitude]




    def GetAltitude(self):
        pass
        #some math to aid readability of air and gravity equations
    def AirResistance(self, velocity, altitude=0, area=1):
        if type(velocity)==type([0]):
            velocity=np.sqrt(sum([component**2 for component in velocity]))
        density = self.AtmosphericDensity(round(altitude))
        drag = 1
        F_air = 1/2 * density * drag * area * velocity**2
        return F_air
    def AtmosphericDensity(self,altitude=0):
        if self.label=="Earth":
            altitude=1000*round(altitude/1000,0)
            if altitude in self.atmosphere.keys():
                return self.atmosphere[altitude]
            else:
                T_o=288.15# Kelvin, sea level standard temperature
                T=T_o-0.0065*altitude #Kelvin, temperature at altitude
                p0=101325 #Pascals, sea level standard atmospheric pressure
                M=0.0289654 #kg/mol, molar mass of dry air
                R=8.31447 #J/(mol·K), ideal (universal) gas constant
                L= 0.0065 #K/m, temperature lapse rate
                g=9.80665 #m/s^2, surface gravity
                if altitude<=18000: #18 km
                    pressure = p0*np.power(1-(L*altitude)/T_o,g*M/(R*L))
                    #MEMOIZE THE RESULTS!
                    density = p0 * M / (R*T_o) * np.power(1-(L*altitude)/T_o,g*M/(R*L)-1)
                elif altitude<83600:
                    density=0.25
                elif 84000>=altitude>=83600:
                    # print("You're probably in space.")
                    density=0.0001
                else:
                    density=0
                self.atmosphere[altitude]=density
                return density