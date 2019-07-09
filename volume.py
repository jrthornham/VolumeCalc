import math

def cuboid():
    
    print("You chose a cuboid")
    
    print("input width")
    value=input()
    w=int(value)

    print("input height")
    value=input()
    h=int(value)

    print("input length")
    value=input()
    l=int(value)
    
    volume=w*h*l
    print("Volume of cuboid is",volume)
    
def sphere():
    
    print("you chose a sphere")
    
    print("Input radius")
    value=input()
    r=int(value)
    
    volume=(4/3)*math.pi*(r**3)
    print("Volume of sphere is",volume)

def cylinder():
    
    print("you chose a cylinder")
    
    print("Input radius")
    value=input()
    r=int(value)
    
    print("Input height")
    value=input()
    h=int(value)
    
    volume=math.pi*(r**2)*h
    print("Volume of cylinder is", volume)