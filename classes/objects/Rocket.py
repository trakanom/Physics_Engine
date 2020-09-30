from .Particle import Particle
class Rocket(Particle):
    #do stuff
    def __init__(self,stages=1):
        self.stages=[self.Add_Stage(stageID=i) for i in range(stages)]
    class Stage:
        def __init__(self,stage_ID,stage_mass,thrust_max,fuel_mass):
            self.stage_ID= stage_ID
            self.stage_mass= stage_mass
            self.thrust_max= thrust_max
            self.fuel_mass=fuel_mass
    def Add_Stage(self,stageID=0,dry_weight=0,wet_weight=0,ISP=0,thrust=0,separable=False,area=1):
        thisRocket = self.stages[stageID]
        thisRocket.dry_weight = dry_weight
        thisRocket.wet_weight = wet_weight
        thisRocket.ISP = ISP
        thisRocket.thrust = thrust
        thisRocket.separable = separable
        thisRocket.area = area
        
    def Engine_Burn(self,thrust_percent,burn_time,stage):
        self.mass-=thrust_percent*self.stages[0].thrust_max
        self.thrust=thrust_percent*self.stages[0].thrust_max
        #TIME THESE WITH ALTITUDE, TIME, OR OTHERWISE. WE CAN SCHEDULE IT **ALL**
    def move(self,time_i,t_res,force=[0,0,0],impulse_frame=[0,0]):
        grav=self.G()
        #include rocket eqn and aerodynamics
        self.velocity=[v+0.5*(g+a+f/self.mass)*np.float_power(t_res,2) for v,a,f,g in zip(self.velocity,self.accel,force,grav)]
        self.position=[round(pos+vel*t_res,3) for pos,vel in zip(self.position,self.velocity)]
        return self.position
    def kinematics(self,F_ext=None):
        if F_ext is None:
            pass
        else:
            pass