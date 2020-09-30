import ast
#https://madhavuniversity.edu.in/types-of-properties-of-engg-materials.html
class Material:
    def __init__(self,name,properties=None):
        self.name = name
        self.properties = {
            'Physical':{
                'density':0,
                'color':None,
                'size':None,
                'shape':None
            },
            'Mechanical':{
                'density':None,
                'hardness':None, #Rockwell B scale 
                'elasticity':None #Modulus of Elasticity (Pascals)
            },

            'Chemical':{},
            'Thermal':{
                'conductivity':None,
                'expansion':None,
                'specific_heat':None,
                'melting_point':None
            },
            'Electrical':{
                'resistance':None
            },
            'Magnetic':{
                'permeability':None
            },
            'Optical':{
                'refraction_index':None
            }

        }
    def addProperties(self,property_type,property_name,property_value):
        self.properties[property_type][property_name] = property_value
    def getProperties(self,props="all"):
        if props=="all":
            for property in self.properties:
                print(property, self.properties[property], sep="\t")
            
if __name__ == '__main__':
    #http://asm.matweb.com/search/SpecificMaterial.asp?bassnum=MQ304L
    steel = Material("304L Stainless Steel")
    steel.addProperties(property_type='Mechanical', property_name='density',property_value=8000) #kg/m^3
    steel.addProperties(property_type='Mechanical', property_name='hardness',property_value=82)
    steel.addProperties(property_type='Mechanical', property_name='elasticity',property_value=(196.5*10**9)) #Pa
    steel.addProperties(property_type='Mechanical', property_name='break_elongation',property_value=0.58) #Percentage
    steel.addProperties(property_type='Mechanical', property_name='tensile_yield',property_value=(210*10**6)) #Pa
    steel.addProperties(property_type='Electrical', property_name='magnetic_permeability',property_value=1.008)
    steel.addProperties(property_type='Thermal', property_name='specific_heat_capacity',property_value=0.5)#J/g degrees C
    steel.addProperties(property_type='Thermal', property_name='melting_point',property_value=[1400,1450]) #Range of temps where it begins its phase change
    steel.addProperties(property_type='Thermal', property_name='Solidus',property_value=1400) #100% Solid below this temp
    steel.addProperties(property_type='Thermal', property_name='Liquidus',property_value=1450) #100% liquid above this temp
    steel.addProperties(property_type='Thermal', property_name='max_service_temp',property_value=870)
    steel.getProperties(props="all")