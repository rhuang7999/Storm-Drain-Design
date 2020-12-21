import math

class StormDrainDesign:
    def __init__(self,name):
        self.name = name
        self.Conversion_Factor, self.Design_flowrate, self.Slope, self.Pipe_material, self.Friction_factor = self.inputs() 

    def inputs(self):
        Manning_number = {'ASPHALT': 0.016, 'BRASS':0.011,'BRICK': 0.015,'DUCTILE IRON': 0.012,'CLAY TILE': 0.014,'CONCRETE': 0.013,
                          'CORRUGATED METAL': 0.022,'GALVANIZED IRON': 0.016,'GLASS': 0.010,'GRAVEL': 0.023,'LEAD': 0.011,'MASONRY': 0.025,
                          'PLASTIC': 0.009,'STEEL': 0.012,'WOOD': 0.012}
        Units = input('Units US or SI: ')
        if Units.upper() == 'US':
            Conversion_factor = float(1.49)
        elif Units.upper() == 'SI':
            print('Convert units to US')
            Covert = input('Are units converted from SI to US? (Y or N): ')
            if Covert.upper() == 'Y':
               Conversion_factor = float(1.49)
            else:
              raise ValueError('Invalid Input! Units must be US')          
        else:
            raise ValueError('Invalid Input! Units must be US')

        Design_flowrate = float(input('Storm Drain Design Flowrate in cfs: '))

        Slope = input('Slope Based on Topographic Conditions (N/A if not given): ')
        if Slope == 'N/A':
            Length = float(input('Length of pipe in feet: '))
            Head_loss = float(input('Headloss in feet: '))
            Slope = Head_loss / Length
            print(Slope)
        else:
            Slope = float(Slope)

        Pipe_material = input('Pipe Material: ')
        if Pipe_material.upper() not in Manning_number:
            raise ValueError("Invalid Input! Material not found")

        Friction_factor = Manning_number[Pipe_material]

        return Conversion_factor, Design_flowrate, Slope, Pipe_material, Friction_factor

    def calc_diameter(self,Q, k, S, n):
        """ Returns the pipe diameter given the 
        units, design flowrate, slope, and Manning's number.
        """
        diameter = ((Q * n * (4 ** (5/3))) / (math.pi * k * (S  ** (1/2)))) ** (3/8)
        #return diameter, diameter * 12 #returns in ft and in inches respecitvely. 
        print('The calculated diameter is:', diameter, 'ft')
        print('The calculated diameter is:', diameter * 12, 'inches')
        return diameter * 12

    #Calcualted_diameter,Diameter_inches = calc_diameter(float(Design_flowrate), Conversion_factor, Slope, Friction_factor)

    #print('The calculated diameter is:', Calcualted_diameter, 'ft')
    #print('The calculated diameter is:', Diameter_inches, 'inches')

    def pipe_diameter(self,d):
        """ Returns the required pipe diameter that would used for the storm drain
        given the calculated diameter in inches.
        """
        if d <= 4:
            d =  4 
        elif d > 4 and d <= 6:
            d = 6
        elif d > 6 and d <= 8:
            d = 8
        elif d > 8 and d <= 10:
            d = 10
        elif d > 10 and d <=12:
            d = 12
        elif d > 12 and d <= 15:
            d = 15
        elif d > 15 and d <= 18:
            d = 18
        elif d > 18 and d <= 21:
            d = 21
        elif d > 21 and d <= 24:
            d = 24
        elif d > 24 and d <= 27:
            d = 27
        elif d > 27 and d <= 30:
            d = 30
        elif d > 30 and d <= 36:
            d = 36
        elif d > 36 and d <= 42:
            d = 42
        elif d > 42 and d <= 48:
            d = 48
        elif d > 48 and d <= 54:
            d = 54
        elif d > 54 and d <= 60:
            d = 60
        elif d > 60 and d <= 66:
            d = 66
        elif d > 66 and d <= 72:
            d = 72
        elif d > 72 and d <= 84:
            d = 84
        elif d > 84 and d <= 90:
            d = 90     
        #return d
        print('For this storm drain a pipe of', d, 'inches should be purchased')
        return d

    #Required_diameter = pipe_diameter(Diameter_inches)
    #print('For this storm drain a pipe of', Required_diameter, 'inches should be purchased')


    def max_flowrate(self,d, k, S, n):
        """ Returns the maximum flowrate of the pipe purchased
        """
        Qmax =  (k / n) * (math. pi * (((d / 12) ** 2) / 4)) * (((d / 12) / 4) ** (2 / 3)) * (S ** (1 / 2))
        print('The maximum flowrate of the pipe is', Qmax, 'cfs')
        return Qmax

    #Qmax = max_flowrate(Required_diameter, Conversion_factor, Slope, Friction_factor)

    #print('The maximum flowrate of the pipe is', Qmax, 'cfs')

    def max_velocity(self,Q, d):
        """ Returns the maximum velocity given the maximum flowrate 
        and pipe diameter
        """
        Vmax = Q / (math. pi * (((d / 12) ** 2) / 4))
        print('The maximum velocity of the pipe is', Vmax, 'ft/s')
        return Vmax

    #Vmax = max_velocity(Qmax, Required_diameter)

    #print('The maximum velocity of the pipe is', Vmax, 'ft/s')

    def main(self):
        Diameter_inches = self.calc_diameter(float(self.Design_flowrate), self.Conversion_Factor, self.Slope, self.Friction_factor)
        Required_diameter = self.pipe_diameter(Diameter_inches)
        Qmax = self.max_flowrate(Required_diameter, self.Conversion_Factor, self.Slope, self.Friction_factor)
        self.max_velocity(Qmax,Required_diameter)
