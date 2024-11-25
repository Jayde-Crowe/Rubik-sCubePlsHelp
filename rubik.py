class Cube:
    def __init__(self, color=None, row=3, col=3):
        # Default when there are no input
        self.affected = []
        if color is None:
            self.faces = {
                'U': [['W']*row for i in range(col)],
                'L': [['G']*row for i in range(col)],
                'F': [['R']*row for i in range(col)],
                'R': [['B']*row for i in range(col)],
                'B': [['O']*row for i in range(col)],
                'D': [['Y']*row for i in range(col)],
            }
        else:
            abc = 0
            self.faces = {}
            face_labels = ['U', 'L', 'F', 'R', 'B', 'D']
            for label in face_labels:
                self.faces[label] = [list(color[abc + a: abc + a + 3]) for a in range(0, 9, 3)]
                abc = abc + 9
            
    def get_color_at(self, face, row, col):
        row = row - 1
        col = col - 1
        possible = {'U', 'L', 'F', 'R', 'B', 'D'}
        if not (0 <= row <= 2 and 0 <= col <= 2):
            raise IndexError(f"Not in [1,1] - [3,3] range: [{row},{col}]")
        if face not in possible:
            raise ValueError(f"{face} is not a face")
        return self.faces[face][row][col]

                        # make sure this last parameter is labeled something that makes sense
    def move(self, face, clockwise):
        self.affected = []
        i = 0
        match face:
            case 'U':
                self._move_up()
                # since a counter clockwise turn is 3 turns, if it is not clockwise we will turn 2 more times
                if not clockwise:
                    for i in range(2):
                        self._move_up()
            case 'L':
                self._move_left()
                if not clockwise:
                    for i in range(2):
                        self._move_left()
            case 'F':
                self._move_front()
                if not clockwise:
                    for i in range(2):
                        self._move_front()
            case 'R':
                self._move_right()
                if not clockwise:
                    for i in range(2):
                        self._move_right()
            case 'B':
                self._move_back()
                if not clockwise:
                    for i in range(2):
                        self._move_back()
            case 'D':
                self._move_down()
                if not clockwise:
                    for i in range(2):
                        self._move_down()


    def _move_back(self):
        # rotate back face top row
        self.faces['B'][0][0] = self.faces['B'][2][0]
        self.faces['B'][0][1] = self.faces['B'][1][0]
        self.faces['B'][0][2] = self.faces['B'][0][0]

        # rotate back face second row
        self.faces['B'][1][0] = self.faces['B'][2][1]
        # middle cell doesn't move
        self.faces['B'][1][2] = self.faces['B'][0][1]

        # rotate back face bottom row
        self.faces['B'][2][0] = self.faces['B'][2][2]
        self.faces['B'][2][1] = self.faces['B'][1][2]
        self.faces['B'][2][2] = self.faces['B'][0][2]

        # save topside 
        topside = [self.faces['U'][0][0], self.faces['U'][0][1], self.faces['U'][0][2]]
        
        # rotate top side
        self.faces['U'][0][0] = self.faces['R'][0][2]
        self.faces['U'][0][1] = self.faces['R'][1][2]
        self.faces['U'][0][2] = self.faces['R'][2][2]
        
        # rotate right side
        self.faces['R'][0][2] = self.faces['D'][2][2]
        self.faces['R'][1][2] = self.faces['D'][2][1]
        self.faces['R'][2][2] = self.faces['D'][2][0]
        
        #rotate bottom side
        self.faces['D'][2][2] = self.faces['L'][2][0]
        self.faces['D'][2][1] = self.faces['L'][1][0]
        self.faces['D'][2][0] = self.faces['L'][0][0]
        
        #rotate left side
        self.faces['L'][0][0] = topside[2]
        self.faces['L'][1][0] = topside[1]
        self.faces['L'][2][0] = topside[0]
        
    def _move_down(self):
        # rotate down face top row
        self.faces['D'][0][0] = self.faces['D'][2][0]
        self.faces['D'][0][1] = self.faces['D'][1][0]
        self.faces['D'][0][2] = self.faces['D'][0][0]

        # rotate down face second row
        self.faces['D'][1][0] = self.faces['D'][2][1]
        # middle cell doesn't move
        self.faces['D'][1][2] = self.faces['D'][0][1]

        # rotate down face bottom row
        self.faces['D'][2][0] = self.faces['D'][2][2]
        self.faces['D'][2][1] = self.faces['D'][1][2]
        self.faces['D'][2][2] = self.faces['D'][0][2]

        # save backside
        backside = [self.faces['B'][2][0], self.faces['B'][2][1], self.faces['B'][2][2]]
        
        # rotate back side
        self.faces['B'][2][0] = self.faces['R'][2][0]
        self.faces['B'][2][1] = self.faces['R'][2][1]
        self.faces['B'][2][2] = self.faces['R'][2][2]
        
        # rotate right side
        self.faces['R'][2][0] = self.faces['F'][2][0]
        self.faces['R'][2][1] = self.faces['F'][2][1]
        self.faces['R'][2][2] = self.faces['F'][2][2]
        
        #rotate front side
        self.faces['F'][2][0] = self.faces['L'][2][0]
        self.faces['F'][2][1] = self.faces['L'][2][1]
        self.faces['F'][2][2] = self.faces['L'][2][2]
        
        #rotate left side
        self.faces['L'][2][0] = backside[0]
        self.faces['L'][2][1] = backside[1]
        self.faces['L'][2][2] = backside[2]
        
    def _move_front(self):
         # rotate front face top row
        self.faces['F'][0][0] = self.faces['F'][2][0]
        self.faces['F'][0][1] = self.faces['F'][1][0]
        self.faces['F'][0][2] = self.faces['F'][0][0]

        # rotate front face second row
        self.faces['F'][1][0] = self.faces['F'][2][1]
        # middle cell doesn't move
        self.faces['F'][1][2] = self.faces['F'][0][1]

        # rotate front face bottom row
        self.faces['F'][2][0] = self.faces['F'][2][2]
        self.faces['F'][2][1] = self.faces['F'][1][2]
        self.faces['F'][2][2] = self.faces['F'][0][2]

        # save topside 
        topside = [self.faces['U'][2][0], self.faces['U'][2][1], self.faces['U'][2][2]]
        
        # rotate top side
        self.faces['U'][2][0] = self.faces['L'][2][2]
        self.faces['U'][2][1] = self.faces['L'][1][2]
        self.faces['U'][2][2] = self.faces['L'][0][2]
        
        # rotate left side
        self.faces['L'][0][2] = self.faces['D'][0][0]
        self.faces['L'][1][2] = self.faces['D'][0][1]
        self.faces['L'][2][2] = self.faces['D'][0][2]
        
        #rotate bottom side
        self.faces['D'][0][0] = self.faces['R'][2][0]
        self.faces['D'][0][1] = self.faces['R'][1][0]
        self.faces['D'][0][2] = self.faces['R'][0][0]
        
        #rotate right side
        self.faces['R'][0][0] = topside[2]
        self.faces['R'][1][0] = topside[1]
        self.faces['R'][2][0] = topside[0]
        
    def _move_left(self):
        # rotate left face top row
        self.faces['L'][0][0] = self.faces['L'][2][0]
        self.faces['L'][0][1] = self.faces['L'][1][0]
        self.faces['L'][0][2] = self.faces['L'][0][0]

        # rotate left face second row
        self.faces['L'][1][0] = self.faces['L'][2][1]
        # middle cell doesn't move
        self.faces['L'][1][2] = self.faces['L'][0][1]

        # rotate left face bottom row
        self.faces['L'][2][0] = self.faces['L'][2][2]
        self.faces['L'][2][1] = self.faces['L'][1][2]
        self.faces['L'][2][2] = self.faces['L'][0][2]

        # save topside 
        topside = [self.faces['U'][0][0], self.faces['U'][1][0], self.faces['U'][2][0]]
        
        # rotate top side
        self.faces['U'][0][0] = self.faces['B'][2][2]
        self.faces['U'][1][0] = self.faces['B'][1][2]
        self.faces['U'][2][0] = self.faces['B'][0][2]
        
        # rotate back side
        self.faces['B'][2][2] = self.faces['D'][0][0]
        self.faces['B'][1][2] = self.faces['D'][1][0]
        self.faces['B'][0][2] = self.faces['D'][2][0]
        
        #rotate bottom side
        self.faces['D'][0][0] = self.faces['F'][0][0]
        self.faces['D'][1][0] = self.faces['F'][1][0]
        self.faces['D'][2][0] = self.faces['F'][2][0]
        
        #rotate froont side
        self.faces['F'][0][0] = topside[0]
        self.faces['F'][1][0] = topside[1]
        self.faces['F'][2][0] = topside[2]
        
    def _move_right(self):
         # rotate right face top row
        self.faces['R'][0][0] = self.faces['R'][2][0]
        self.faces['R'][0][1] = self.faces['R'][1][0]
        self.faces['R'][0][2] = self.faces['R'][0][0]

        # rotate right face second row
        self.faces['R'][1][0] = self.faces['R'][2][1]
        # middle cell doesn't move
        self.faces['R'][1][2] = self.faces['R'][0][1]

        # rotate right face bottom row
        self.faces['R'][2][0] = self.faces['R'][2][2]
        self.faces['R'][2][1] = self.faces['R'][1][2]
        self.faces['R'][2][2] = self.faces['R'][0][2]

        # save topside 
        topside = [self.faces['U'][2][2], self.faces['U'][1][2], self.faces['U'][0][2]]
        
        # rotate top side
        self.faces['U'][2][2] = self.faces['F'][2][2]
        self.faces['U'][1][2] = self.faces['F'][1][2]
        self.faces['U'][0][2] = self.faces['F'][0][2]
        
        # rotate front side
        self.faces['F'][2][2] = self.faces['D'][2][2]
        self.faces['F'][1][2] = self.faces['D'][1][2]
        self.faces['F'][0][2] = self.faces['D'][0][2]
        
        #rotate bottom side
        self.faces['D'][0][2] = self.faces['B'][2][0]
        self.faces['D'][1][2] = self.faces['B'][1][0]
        self.faces['D'][2][2] = self.faces['B'][0][0]
        
        #rotate back side
        self.faces['B'][0][0] = topside[0]
        self.faces['B'][1][0] = topside[1]
        self.faces['B'][2][0] = topside[2]
    
    def _move_up(self):
         # rotate up face top row
        self.faces['U'][0][0] = self.faces['U'][2][0]
        self.faces['U'][0][1] = self.faces['U'][1][0]
        self.faces['U'][0][2] = self.faces['U'][0][0]

        # rotate up face second row
        self.faces['U'][1][0] = self.faces['U'][2][1]
        # middle cell doesn't move
        self.faces['U'][1][2] = self.faces['U'][0][1]

        # rotate up face bottom row
        self.faces['U'][2][0] = self.faces['U'][2][2]
        self.faces['U'][2][1] = self.faces['U'][1][2]
        self.faces['U'][2][2] = self.faces['U'][0][2]

        # save backside
        topside = [self.faces['B'][0][0], self.faces['B'][0][1], self.faces['B'][0][2]]
        
        # rotate back side
        self.faces['B'][0][2] = self.faces['L'][0][2]
        self.faces['B'][0][1] = self.faces['L'][0][1]
        self.faces['B'][0][0] = self.faces['L'][0][0]
        
        # rotate left side
        self.faces['L'][0][0] = self.faces['F'][0][0]
        self.faces['L'][0][1] = self.faces['F'][0][1]
        self.faces['L'][0][2] = self.faces['F'][0][2]
        
        #rotate front side
        self.faces['F'][0][0] = self.faces['R'][0][0]
        self.faces['F'][0][1] = self.faces['R'][0][1]
        self.faces['F'][0][2] = self.faces['R'][0][2]
        
        #rotate back side
        self.faces['R'][0][0] = topside[0]
        self.faces['R'][0][1] = topside[1]
        self.faces['R'][0][2] = topside[2]



def main(args):
    pass


if '__main__' == __name__:
    import sys
    main(sys.argv)
