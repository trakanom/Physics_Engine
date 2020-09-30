import numpy as np
import time
import matplotlib.pyplot as plt
import profile
Program_Start=time.time()
from classes.tools.Coordinates import Coordinates
from classes.tools.physical_constants import gravitational_constant
from classes.objects.Particle import Particle
from classes.objects.Celestial_Body import Celestial_Body


# def FlyMyPretties(MyObjects):
#     #Firstly, we have the object in question
#     #Second, we have the positional argument
#     #Last, the iterative component
#     myPos=[
#         [
#         [MyObjects[n].move(time_i=t,t_step=t_step)
#          for t in range(t_start,round(t_finish/t_step)+1)]
#          for i in range(len(MyObjects[n].position))]
#           for n in range(len(MyObjects))
#           ]
#     print(myPos)
#     return(myPos)
def FlyMyPretties(MyObjects):
    # myX=[]
    # myY=[]
    # myZ=[]
    # myPos=[]
    for t in range(t_start,round(t_finish/t_step)+1):
        thisTime = round(t*t_step,2)
        myForce = [0,0,65000000] #[x,y,z] Newtons, [t_0,t_f] seconds
        i_frame = [0,6*600] #Will be active from 0 to 3600 seconds.
        # aPos = MyObjects[0].move(time_i=t,t_step=t_step,)
        aPos = MyObjects[0].move(time_i=t,t_step=t_step,force=(myForce if i_frame[0]<=thisTime<=i_frame[1] else [0,0,0]))
        # myPos.append(aPos)
        # print(aPos[0])
        # myX.append(aPos[0])
        # myY.append(aPos[1])
        # myZ.append(aPos[2])
    print(*[MyObject.path[1:] for MyObject in MyObjects])
    return([MyObject.path[1:] for MyObject in MyObjects])



def graphMe(xyzList):
    xyzList=xyzList[0]
    #This just prints a graph.
    x = np.array(xyzList[0])
    y = np.array(xyzList[1])
    z = np.array(xyzList[2])
    # print(x,y,z,sep="\n")
    t=np.arange(0,round(t_finish/t_step+1),1)
    plt.plot(t,x,t,y,t,z)
    plt.title('Trajectory')
    plt.xlabel('time(s)')
    plt.ylabel('position(m)')
    plt.grid(True)
    plt.show()

if __name__ == '__main__':
    # origin = [0,0,0] #[x,y,z] meters
    #settings are mocking SpaceX's Starship specs.
    Earth = Celestial_Body(label="Earth", mass=5.972*10**24, radius=6.371*10**6, atmosphere=True)
    Starship = Particle(label = "Starship", mass = 5000000, position=[0,0,100], velocity=[0,0,10], type="Cartesian", primary_body=Earth,elasticity=0.5)
    #Time start, finish, and time resolution per step
    MovingObjects = [Starship]
    t_start = 0 #seconds
    t_finish = 10*60**2 #seconds
    t_step = 0.1 #seconds per iteration


    # print(Earth.AtmosphericDensity(1),Earth.AirResistance(velocity=[10,5],altitude=17800,area=1))
    results = FlyMyPretties(MovingObjects)
    Prog_end=time.time()
    print(f"Runtime={Prog_end-Program_Start}")
    graphMe(results)

    # print(*Starship.path,sep="\n")


















'''
    TO-DO:
        Physics
            Interactions
                Bouncing
                Collisions
                Boundaries

        Celestial Bodies
            Orbital
                Transfer Orbits
            Solar System
                Sun
                Earth
                Moon
                Mars
                Venus
        
        Structure
            "One class per file"
            Physics.py
            /resources
                /Celestial Bodies
                    /Earth
                        /data (memoized)
                            air_density
                            gravity
                /Physics
                    orbitals
                    kinematics
                    fluids?
        Documentation
            DO IT
            
'''