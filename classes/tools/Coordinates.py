class Coordinates:
    def __init__(self,type, position=None):
        self.type = type
        if self.type == "Cartesian":
            self.position=position
            self.Cartesian(position=position)
        elif self.type == "Spherical":
            pass
        elif self.type == "Polar":
            pass
        elif self.type == "Lorentz":
            pass
        elif self.type == "Cylindrical":
            pass
    

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