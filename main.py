class Cube():
    
    def __init__(self, trichord):
        self.trichord = trichord
        self.cube = list()

    def populate_cube(self):
        for part in range(2):
            cube_side = []
            for side in range(4): 
                cube_side.append(self.trichord)
            self.cube.append(cube_side)
    
    def modify_cube(self):
        init = False
        for idx in range(len(self.cube)):
            if idx == 1:
                break
            for iter, chord in enumerate(self.cube[idx]):
                if iter == 0 and idx == 0:
                    continue
                for pch_idx in range(len(chord)):
                    if pch_idx == iter:
                        print(f'looking at pitch {chord[pch_idx]} in chord number {iter} in side {idx}')
                        chord[pch_idx] = chord[pch_idx] - 1



    def change_cell(self, item, index):
        item[index] =- 1
        return item

                

    def print_cube(self):
        print(self.cube)


cube = Cube([9,5,1])

cube.populate_cube()
cube.modify_cube()
cube.print_cube()
