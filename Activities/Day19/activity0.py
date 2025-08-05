'''diameter=2r
circumference=2pir
area=2pir**2
'''
import math
radius=int(input("enter the radius of the circle:"))
diameter=2*radius
circumference=math.floor(2*math.pi*radius)
area=math.ceil(2*math.pi*(radius**2))
print(f'For a radis of {radius}\nDiameter:{diameter}\nCircumference : {circumference}\nArea:{area}')