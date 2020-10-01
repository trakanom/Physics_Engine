class Coordinates:
    def __init__(self,type=None, position=None):
        if position is None:
            position=tuple([0,0,0])
        if type is None:
            type = "Cartesian"
        self.type = type
        if self.type == "Cartesian":
            if not isinstance(position,list):
                position = tuple([0,0,0])
            self.x = position[0]
            self.y = position[1]
            self.z = position[2]
            self.position=tuple([self.x, self.y, self.z])
            # self.Cartesian(position=position)
        elif self.type == "Spherical":
            if not isinstance(position,list):
                position = tuple([0,0,0])
            self.rho = position[0]
            self.theta = position[1]
            self.phi = position[2]
            self.position = tuple([self.rho, self.theta, self.phi]) 
        elif self.type == "Polar":
            if not isinstance(position,list):
                position = tuple([0,0,0])
        elif self.type == "Lorentz":
            pass
        elif self.type == "Cylindrical":
            if not isinstance(position,list):
                position = tuple([0,0,0])
    

    # def Spherical(self,rho=1,theta=0,phi=0, ):
    #     self.rho = rho
    #     self.theta = theta
    #     self.phi = phi
    # def Cartesian(self,x=None,y=None,z=None,position=None): #Minimum 1 dimension.
    #     if x == None and y == None and z == None and position == None:
    #         print("oh no")
    #         self.x = x
    #         self.y = y
    #         self.z = z
    #         self.position = position
    #     else:
    #         self.position = position if position!=None else [x,y,z]
    #         self.x = x if position == None else position[0]
    #         self.y = y if position == None else position[1]
    #         self.z = z if position == None else position[2]
    # def Polar(self,r=1,theta=0):
    #     self.r = r
    #     self.theta = theta
    # def Lorentz(self,Lorentz=None):
    #     print("Hey, let's not go to relativistic speeds until we finish the basics. Thanks.")
    #     pass
    #     #hey, maybe make a relativity KSP mod?
    def CartesianToPolar(self):
        pass
    def PolarToCartesian(self):
        pass
    def CartesianToSpherical(self):
        pass
    def SphericalToCartesian(self):
        pass