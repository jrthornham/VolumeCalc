import volume

def shapecalculator():
    
    print("""
      
          Please choose a shape and type the corresponding number;
          1.cuboid
          2.sphere
          3.cylinder
          
          """)

    choice=input()
    choice=int(choice)

    if choice == 1:

        volume.cuboid()

    if choice == 2:
    
        volume.sphere()

    if choice == 3:
    
        volume.cylinder()