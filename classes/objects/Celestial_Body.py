import sys
sys.path.append('..')
from ..tools.Coordinates import Coordinates
class Celestial_Body(Coordinates):
    def __init__(self,name="Earth"):
        self.name= name
        if self.name=="Earth":
            self.mass=(5.972*10**24)
            self.radius=6.371*10**6
            self.atmosphere={}
            self.gravity={}
    def populateConstants(self,entries):
        for i in range(entries):
            print(f"Dicts populating...\t{round(i/entries)}% ({i}/{entries}).")
            self.AtmosphericDensity(i)
            self.GravitationalForce(i)
        
    def GravitationalForce(self):
        pass
        #gravitystuff
    def GetAltitude(self):
        pass
        #some math to aid readability of air and gravity equations
    def AirResistance(self, velocity, altitude=0, area=1):
        density = self.AtmosphericDensity(round(altitude))
        drag = 1
        F_air = 1/2 * density * drag * area * velocity**2
    def AtmosphericDensity(self,altitude=0):
        if self.name=="Earth":
            if altitude in self.atmosphere.keys():
                return self.atmosphere[altitude]
            else:
                if altitude<=18000: #18 km
                    T_0=288.15# Kelvin, sea level standard temperature
                    T=T_0-0.0065*altitude #Kelvin, temperature at altitude
                    p0=101325 #Pascals, sea level standard atmospheric pressure
                    M=0.0289654 #kg/mol, molar mass of dry air
                    R=8.31447 #J/(mol·K), ideal (universal) gas constant
                    #MEMOIZE THE RESULTS!
                else:
                    print("You're probably in space.")
                self.atmosphere[altitude]=density
                return density