import numpy as np
import time
import matplotlib.pyplot as plt
class Particle:
    def __init__(self, label, mass=None, position=None, velocity=[0,0,0], elasticity = 1):
        self.label=label
        self.mass = mass
        self.position = position
        self.velocity = velocity
        self.x = self.position[0]
        self.y = self.position[1]
        self.z = self.position[2]
    def pos(self,time_i,t_res,force=[0,0,0],impulse_frame=[0,0]):
        grav=self.G()
        # grav = [0,0,(np.power(
        #     self.position[3]+6.3781*(10**6),2
        # ))]
        # print(grav)
        self.velocity=[v+0.5*(g+a+f/self.mass)*np.float_power(t_res,2) for v,a,f,g in zip(self.velocity,self.accel,force,grav)]
        self.position=[round(pos+vel*t_res,3) for pos,vel in zip(self.position,self.velocity)]
        return self.position
    def G(self):
        m1 = 5.972*(10**24)
        earth = 6.3781*(10**6)
        gConst = 6.673/(10**11)
        grav = [0,0,-(gConst*m1)/(np.power(self.position[2]+6.3781*(10**6),2))]
        print(f"gravity at {self.position}: {grav[-1]}")
        return grav
        # print(m1,self.mass,core,gConst*m1*self.mass)
        # base = np.format_float_scientific(np.float32(6.3781e6))
        # base = np.power(np.sqrt(
            
        #         sum(
        #     [np.power((component-core),2) for core,component in zip(earth,self.position)]
        #             )
                
        # ),2)
        # print(base)
        # print("wtf is going on,",[np.power(component,2) for component in self.position])
        # print(f"gravity = {grav} m/s*s")
        #THESE RESULTS ARE FORCE. NOT. ACCELERATION. FIX. THIS.

class Bounds:
    def __init__(self, label, position=(None), isPlane=False, pFunct=None):
        self.label = label
        self.position = position
        self.isPlane = isPlane
        
# gConst = np.format_float_scientific(np.float32(6.673e-11))
gConst = 6.673/(10**11)
origin = [0,0,0] #[x,y,z] meters
p1 = Particle(label = "p1", mass = 5000000, position=[0,0,80000], velocity=[0,0,0])
p1.accel = [0,0,0] #[x,y,z] meters/sec**2
ground = Bounds(label = "ground", position=origin, isPlane = True, pFunct = [0,0,None])
wall = Bounds(label = "wall", position=origin, isPlane=True, pFunct=[None,None,0])
t_start = 0 #seconds
t_finish = 60**2 #seconds
t_res = 0.1 #seconds per iteration
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

# myTimes = np.arange(0,101,1,dtype=int)
x = np.array(myX)
y = np.array(myY)
z = np.array(myZ)
# print(x,y,z,sep="\n")
# print(*zip(myX,myY,myZ),sep="\n")
t=np.arange(0,round(t_finish/t_res+1),1)
# print(t.shape)
# print(myX)

# x=myX[t]
# y=myY[t]
# z=myZ[t]

plt.plot(t,x,t,y,t,z)
plt.title('UHHHHHHHHH')
plt.grid(True)
plt.show()
# p1.mass = 0.001 #kg
# p1.position = (0,0,0)