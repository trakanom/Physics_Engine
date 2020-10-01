import sys
import numpy as np
from ..tools.Coordinates import Coordinates
from ..tools.physical_constants import GRAVITATIONAL_CONSTANT
class Celestial_Body(Coordinates):
    def __init__(self,label=None,mass=0,radius=0, atmosphere=None, type=None, position=None, primary_body=None, velocity=None):
        self.label = label
        self.mass=mass
        self.radius=radius
        self.gravity={}
        if isinstance(velocity,list) or isinstance(velocity,tuple):
            self.velocity = velocity
        else:
            self.velocity = tuple([0,0,0])
        if atmosphere:
            self.atmosphere={}
        else:
            self.atmosphere=False
        self.populateConstants(1000)
        super().__init__(type, position)
    def populateConstants(self,entries):
        for i in range(entries):
            # print(f"Dicts populating...\t{round(100*i/entries)}% ({i}/{entries}).")
            i=1000*i
            self.GravitationalForce(i)
            if self.atmosphere:
                self.AtmosphericDensity(i)
        # print(*zip(self.gravity.keys(),self.gravity.values(),self.atmosphere.values()), sep="\n")
    def GravitationalForce(self,altitude):
        altitude_nearest_km = round(altitude,-3)
        # gConst = 6.673/(10**11)
        if altitude_nearest_km in self.gravity.keys():
            return self.gravity[altitude_nearest_km]
        else:
            # print(f"GRAVITY NOT FOUND AT {altitude_nearest_km}km, recalculating!")
            self.gravity[altitude_nearest_km] = -(GRAVITATIONAL_CONSTANT*self.mass)/(np.power(altitude_nearest_km+self.radius,2))
            # print(f"gravity at {altitude_nearest_km}: {gravity[altitude_nearest_km]}")
            return self.gravity[altitude_nearest_km]
    def orbit(self):
        pass
    def AirResistance(self, velocity, altitude=0, area=1):
        if isinstance(velocity, list):
            velocity=np.sqrt(sum([component**2 for component in velocity]))
        density = self.AtmosphericDensity(round(altitude))
        drag = 1
        F_air = 1/2 * density * drag * area * velocity**2
        return F_air
    def AtmosphericDensity(self,altitude=0):
        if self.label=="Earth":

            altitude_nearest_km = round(altitude,-3)
            if altitude_nearest_km in self.atmosphere.keys():
                return self.atmosphere[altitude_nearest_km]
            else:
                T_o=288.15# Kelvin, sea level standard temperature
                T=T_o-0.0065*altitude_nearest_km #Kelvin, temperature at altitude_nearest_km
                p0=101325 #Pascals, sea level standard atmospheric pressure
                M=0.0289654 #kg/mol, molar mass of dry air
                R=8.31447 #J/(mol·K), ideal (universal) gas constant
                L= 0.0065 #K/m, temperature lapse rate
                g=9.80665 #m/s^2, surface gravity
                if altitude_nearest_km<=18000: #18 km
                    pressure = p0*np.power(1-(L*altitude_nearest_km)/T_o,g*M/(R*L))
                    #MEMOIZE THE RESULTS!
                    density = p0 * M / (R*T_o) * np.power(1-(L*altitude_nearest_km)/T_o,g*M/(R*L)-1)
                elif altitude_nearest_km<83600:
                    density=0.25
                elif 84000>=altitude_nearest_km>=83600:
                    # print("You're probably in space.")
                    density=0.0001
                else:
                    density=0
                self.atmosphere[altitude_nearest_km]=density
                return density