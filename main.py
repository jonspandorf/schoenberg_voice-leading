

import numbers


class Cube():
    
    def __init__(self, trichord):
        self.trichord = trichord
        self.cube = list()

    def populate_cube(self):
        for part in range(2):
            cube_side = []
            for side in range(2): 
                cube_side.append(self.trichord)
            self.cube.append(cube_side)
    
    def modify_cube(self):
        for index in range(len(self.cube)):
            for item, num in enumerate(self.cube[index]):
                print(item, num)

    def print_cube(self):
        print(self.cube)


cube = Cube([0,4,8])

cube.populate_cube()
cube.modify_cube()
