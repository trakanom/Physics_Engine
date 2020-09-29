import numpy as np
import time
import matplotlib.pyplot as plt
class Coordinates:
    def __init__(self,type, position=None):
        self.type = type
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
    def AddXYZ(self,position):
        if self.position==None:
            self.position= position
        self.x = position[0]
        self.y = position[1]
        self.z = position[2]
        print(self.position,self.x, self.y, self.z)
    def Spherical(self,rho=1,theta=0,phi=0):
        self.rho = rho
        self.theta = theta
        self.phi = phi
    def Cartesian(self,x=None,y=None,z=None,position=None): #Minimum 1 dimension.
        if x == None and y == None and z == None and position == None:
            print("oh no")
            self.x = x
            self.y = y
            self.z = z
            self.position = position
        else:
            self.position = position if position!=None else [x,y,z]
            self.x = x if position == None else position[0]
            self.y = y if position == None else position[1]
            self.z = z if position == None else position[2]
    def Polar(self,r=1,theta=0):
        self.r = r
        self.theta = theta
    def Lorentz(self,Lorentz=None):
        print("Hey, let's not go to relativistic speeds until we finish the basics. Thanks.")
        pass
        #hey, maybe make a relativity KSP mod?
    def CartesianToPolar(self):
        pass
    def PolarToCartesian(self):
        pass
    def CartesianToSpherical(self):
        pass
    def SphericalToCartesian(self):
        pass

class Particle(Coordinates):
    def __init__(self, label, mass=None, position=[0,0,0], velocity=[0,0,0], type="Cartesian"):
        self.label=label
        self.mass = mass
        self.type = type
        self.velocity = velocity
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
        # self.position = position
        # self.velocity = velocity
                                    # if coord_system!=None:
                                    #     if self.coord_system == "Cartesian":
                                    #         print("Cartesian Coordinate System")
                                    #         # self.coord_system =  Coordinates(type="Cartesian",position=self.position)
                                    #         self.position = Coordinates(type=self.coord_system,position=position)
                                    #         # self.position.AddXYZ(position)
                                    #         print("in particle: ",self.position)
                                    #         self.velocity = Coordinates(type=self.coord_system,position=velocity)
                                    #     elif self.coord_system == 'Spherical':
                                    #         print("Spherical Coordinate System")
                                    #         self.position=Coordinates.Spherical(position)
                                    #         self.position=Coordinates.Spherical(velocity)
                                    #     elif self.coord_system == 'Polar':
                                    #         print("Polar Coordinate System")
                                    #         self.position=Coordinates.Polar(position)
                                    #         self.position=Coordinates.Polar(velocity)
                                    #     elif self.coord_system == 'Lorentz':
                                    #         print("Would you kindly don't?")
                                    #     else:
                                    #         print("Error: Invalid coordinate system. Please try again.")
    def pos(self,time_i,t_res,force=[0,0,0],impulse_frame=[0,0]):
        grav=self.G()
        self.velocity=[v+0.5*(g+a+f/self.mass)*np.float_power(t_res,2) for v,a,f,g in zip(self.velocity,self.accel,force,grav)]
        self.position=[round(pos+vel*t_res,3) for pos,vel in zip(self.position,self.velocity)]
        return self.position
    def G(self):
        m1 = 5.972*(10**24)
        earth = 6.3781*(10**6)
        gConst = 6.673/(10**11)
        grav = [0,0,-(gConst*m1)/(np.power(self.z+6.3781*(10**6),2))]
        print(f"gravity at {self.position}: {grav[-1]}")
        return grav
class Bounds:
    def __init__(self, label, position=(None), isPlane=False, pFunct=None):
        self.label = label
        self.position = position
        self.isPlane = isPlane



gConst = 6.673/(10**11)
origin = [0,0,0] #[x,y,z] meters
#settings are mocking SpaceX's Starship specs.
p1 = Particle(label = "p1", mass = 5000000, position=[0,0,0], velocity=[0,0,10], type="Cartesian")
p1.accel = [0,0,0] #[x,y,z] meters/sec**2
ground = Bounds(label = "ground", position=origin, isPlane = True, pFunct = [0,0,None])
wall = Bounds(label = "wall", position=origin, isPlane=True, pFunct=[None,None,0])
t_start = 0 #seconds
t_finish = 60**2 #seconds
t_res = 0.1 #seconds per iteration
# myForce = [0,0,10] #[x,y,z] Newtons, [t_0,t_f] seconds
# i_frame = [0,1]
myForce = [65000000*0.25*0.02,0,.98*65000000] #[x,y,z] Newtons, [t_0,t_f] seconds
i_frame = [0,3*600]
myX=[]
myY=[]
myZ=[]
for t in range(t_start,round(t_finish/t_res)+1):
    thisTime = round(t*t_res,2)
    # thisPos.append(p1.pos(time_i=t,t_res=t_res,force=(myForce if i_frame[0]<=thisTime<=i_frame[1] else [0,0,0]))+[thisTime])
    thrustshit = (myForce if i_frame[0]<=thisTime<=i_frame[1] else [0,0,0])
    aPos = p1.pos(time_i=t,t_res=t_res,force=(myForce if i_frame[0]<=thisTime<=i_frame[1] else [0,0,0]))
    # print(aPos[0])
    myX.append(aPos[0])
    myY.append(aPos[1])
    myZ.append(aPos[2])
    print("time=",thisTime,"position=",aPos)

x = np.array(myX)
y = np.array(myY)
z = np.array(myZ)
t=np.arange(0,round(t_finish/t_res+1),1)

plt.plot(t,x,t,y,t,z)
plt.title('Trajectory')
plt.xlabel('time(s)')
plt.ylabel('position(m)')
plt.grid(True)
plt.show()