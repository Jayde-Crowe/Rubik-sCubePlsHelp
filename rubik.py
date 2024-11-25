class Cube:
    def __init__(self, color=None, row=3, col=3):
        # Default when there are no input
        self.affected = []
        self.rotation = True
        self.labels = []
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
            print(color)
            no_space = color.replace(" ", "")
            print(no_space)
            if (len(no_space) != 54):
                raise ValueError("Cube must have 54 cubletes")
            abc = 0
            self.faces = {}
            face_labels = ['U', 'L', 'F', 'R', 'B', 'D']
            for label in face_labels:
                self.faces[label] = [list(no_space[abc + a: abc + a + 3]) for a in range(0, 9, 3)]
                abc = abc + 9
            # self.print_cube_layout()

    def get_color_at(self, face, row, col):
        row = row - 1
        col = col - 1
        possible = {'U', 'L', 'F', 'R', 'B', 'D'}
        if not (0 <= row <= 2 and 0 <= col <= 2):
            raise IndexError(f"Not in [1,1] - [3,3] range: [{row},{col}]")
        if face not in possible:
            raise ValueError(f"{face} is not a face")
        return self.faces[face][row][col]

    def set_cube(self, string):
        data = string.split()

        # Remove the single characters at the end
        data2 = [string for string in data if len(string) == 9]
        print(data2)

        if len(data2) != 6:
            raise ValueError(f"Six != {len(data2)}")
        for element in data2:
            if len(element) != 9:
                raise ValueError(f"Nine != {len(element)}")
        for f in range(6):
            index = 0
            for x in range(3):
                for y in range(3):
                    match f:
                        case 0:
                            face = 'U'
                        case 1:
                            face = 'L'
                        case 2:
                            face = 'F'
                        case 3:
                            face = 'R'
                        case 4:
                            face = 'B'
                        case 5:
                            face = 'D'
                    self.faces[face][x][y] = data[f][index]
                    index = index + 1

    def move(self, face, rotation):
        self.rotation = rotation
        self.affected = []
        self.labels = []
        if (rotation):
            x = 1
        else:
            x = 3
        match face:
            case 'U':
                while (x != 0):
                    self.rotation_up()
                    self.__move_up()
                    x = x - 1
            case 'L':
                while (x != 0):
                    self.rotation_left()
                    self.__move_left
                    x = x - 1
            case 'F':
                while (x != 0):
                    self.rotation_front()
                    self.__move_front()
                    x = x - 1
            case 'R':
                while (x != 0):
                    self.rotation_right()
                    self.__move_right()
                    x = x - 1
            case 'B':
                while (x != 0):
                    self.rotation_back()
                    self.__move_back()
                    x = x - 1
            case 'D':
                while (x != 0):
                    self.rotation_down()
                    self.__move_down()
                    x = x - 1
            case _:
                raise ValueError(f"{face} is not a face")
        # print(f"affected: {self.affected}")

    def rotation_up(self):
        # Save Left Side Values
        temp_1 = self.faces['L'][0][2]
        # Back Corner
        temp_2 = self.faces['L'][0][1]
        # Middle
        temp_3 = self.faces['L'][0][0]
        # Front Corner

        # Update Left
        self.faces['L'][0][2] = self.faces['F'][0][0]
        # Back Corner = Left Corner
        self.faces['L'][0][1] = self.faces['F'][0][1]
        # Middle = Middle
        self.faces['L'][0][0] = self.faces['F'][0][2]
        # Front Corner = Right Corner

        # Update Front
        self.faces['F'][0][0] = self.faces['R'][0][0]
        # Left Corner = Front Corner
        self.faces['F'][0][1] = self.faces['R'][0][1]
        # Middle = Middle
        self.faces['F'][0][2] = self.faces['R'][0][2]
        # Right Corner = Back Corner

        # Update Right
        self.faces['R'][0][0] = self.faces['B'][0][2]
        # Front Corner = Right Corner
        self.faces['R'][0][1] = self.faces['B'][0][1]
        # Middle = Middle
        self.faces['R'][0][2] = self.faces['B'][0][0]
        # Back Corner = Left Corner

        # Update Back
        self.faces['B'][0][2] = temp_1
        # Right Corner = Back Corner
        self.faces['B'][0][1] = temp_2
        # Middle = Middle
        self.faces['B'][0][0] = temp_3
        # Left Corner = Front Corner

    def rotation_left(self):
        # Coded CCW instead of CW
        for i in range(3):
            # Save Top Values
            temp1 = self.faces['U'][0][0]
            # Back Corner
            temp2 = self.faces['U'][1][0]
            # Middle
            temp3 = self.faces['U'][2][0]
            # Front Corner

            # Update Top
            self.faces['U'][0][0] = self.faces['F'][0][0]
            # Back Corner = Top
            self.faces['U'][1][0] = self.faces['F'][1][0]
            # Middle = Middle
            self.faces['U'][2][0] = self.faces['F'][2][0]
            # Front Corner = Bottom Corner

            # Update Front
            self.faces['F'][0][0] = self.faces['D'][0][0]
            # Top = Front Corner
            self.faces['F'][1][0] = self.faces['D'][1][0]
            # Middle = Middle
            self.faces['F'][2][0] = self.faces['D'][2][0]
            # Bottom = Back Corner

            # Update Bottom
            self.faces['D'][0][0] = self.faces['B'][2][2]
            # Front Corner = Bottom
            self.faces['D'][1][0] = self.faces['B'][1][2]
            # Middle = Middle
            self.faces['D'][2][0] = self.faces['B'][0][2]
            # Back Corner = Top

            self.faces['B'][2][2] = temp1
            # Bottom = Back Corner
            self.faces['B'][1][2] = temp2
            # Middle = Middle
            self.faces['B'][0][2] = temp3
            # Top = Front Corner

    def rotation_back(self):
        # CWW instead of CW
        for i in range(3):
            # Store Top Value
            temp1 = self.faces['U'][0][0]
            temp2 = self.faces['U'][0][1]
            temp3 = self.faces['U'][0][2]

            # Update Top
            self.faces['U'][0][0] = self.faces['L'][2][0]
            # Left Corner = Bottom
            self.faces['U'][0][1] = self.faces['L'][1][0]
            # Middle = Middle
            self.faces['U'][0][2] = self.faces['L'][0][0]
            # Right Corner = Top

            # Update Left
            self.faces['L'][2][0] = self.faces['D'][2][2]
            # Bottom = Right Corner
            self.faces['L'][1][0] = self.faces['D'][2][1]
            # Middle = Middle
            self.faces['L'][0][0] = self.faces['D'][2][0]
            # Top = Left Corner

            # Update Bottom
            self.faces['D'][2][2] = self.faces['R'][0][2]
            # Right Corner = Top
            self.faces['D'][2][1] = self.faces['R'][1][2]
            # Middle = Middle
            self.faces['D'][2][0] = self.faces['R'][2][2]
            # Left Corner = Bottom

            # Update Right
            self.faces['R'][0][2] = temp1
            # Top = Left Corner
            self.faces['R'][1][2] = temp2
            # Middle = Middle
            self.faces['R'][2][2] = temp3
            # Bottom = Right Corner

    def rotation_down(self):
        for i in range(3):
            # Save Left Side
            temp1 = self.faces['L'][2][2]
            temp2 = self.faces['L'][2][1]
            temp3 = self.faces['L'][2][0]

            # Update Left Side
            self.faces['L'][2][2] = self.faces['F'][2][0]
            # Front Corner = Right Corner
            self.faces['L'][2][1] = self.faces['F'][2][1]
            # Middle = Middle
            self.faces['L'][2][0] = self.faces['F'][2][2]
            # Back Corner = Left Corner

            # Update Front Side
            self.faces['F'][2][2] = self.faces['R'][2][2]
            # Right Corner = Back
            self.faces['F'][2][1] = self.faces['R'][2][1]
            # Middle = Middle
            self.faces['F'][2][0] = self.faces['R'][2][0]
            # Left Corner = Front

            # Update Right Side
            self.faces['R'][2][2] = self.faces['B'][2][0]
            # Back = Left Corner
            self.faces['R'][2][1] = self.faces['B'][2][1]
            # Middle = Middle
            self.faces['R'][2][0] = self.faces['B'][2][2]
            # Front = Right Corner

            # Update Back
            self.faces['B'][2][2] = temp1
            # Right Corner = Front
            self.faces['B'][2][1] = temp2
            # Middle = Middle
            self.faces['B'][2][0] = temp3
            # Left Corner = Back

    def rotation_right(self):

        # Save Front Values
        temp1 = self.faces['F'][0][2]
        temp2 = self.faces['F'][1][2]
        temp3 = self.faces['F'][2][2]

        # Update Front Values
        self.faces['F'][0][2] = self.faces['D'][0][2]
        # Top = Front
        self.faces['F'][1][2] = self.faces['D'][1][2]
        # Middle = Middle
        self.faces['F'][2][2] = self.faces['D'][2][2]
        # Bottom = Back

        # Update Bottom Values
        self.faces['D'][0][2] = self.faces['B'][2][0]
        # Front = Bottom
        self.faces['D'][1][2] = self.faces['B'][1][0]
        # Middle = Middle
        self.faces['D'][2][2] = self.faces['B'][0][0]
        # Back = Top

        # Update Back Values
        self.faces['B'][2][0] = self.faces['U'][0][2]
        self.faces['B'][1][0] = self.faces['U'][1][2]
        self.faces['B'][0][0] = self.faces['U'][2][2]

        # Update Top Values
        self.faces['U'][0][2] = temp1
        self.faces['U'][1][2] = temp2
        self.faces['U'][2][2] = temp3

    def rotation_front(self):
        # Save Top Values
        temp1 = self.faces['U'][2][0]
        temp2 = self.faces['U'][2][1]
        temp3 = self.faces['U'][2][2]

        # Update Top Vales
        self.faces['U'][2][0] = self.faces['L'][2][2]
        # Left Corner = Bottom
        self.faces['U'][2][1] = self.faces['L'][1][2]
        # Middle = Middle
        self.faces['U'][2][2] = self.faces['L'][0][2]
        # Right Corner = Top

        # Update Left Side
        self.faces['L'][2][2] = self.faces['D'][0][2]
        # Bottom = Right Corner
        self.faces['L'][1][2] = self.faces['D'][0][1]
        # Middle = Middle
        self.faces['L'][0][2] = self.faces['D'][0][0]
        # Top = Left Corner

        # Update Bottom Side
        self.faces['D'][0][2] = self.faces['R'][0][0]
        # Right Corner = Top
        self.faces['D'][0][1] = self.faces['R'][1][0]
        # Middle = Middle
        self.faces['D'][0][0] = self.faces['R'][2][0]
        # Left Corner = Bottom

        # Update Right Side
        self.faces['R'][0][0] = temp1
        # Top = Left Corner
        self.faces['R'][1][0] = temp2
        # Middle = Middle
        self.faces['R'][2][0] = temp3
        # Bottom = Right Corner

    def rotation_clockwise(self, face):
        # Rotate Corners
        # print(f"face: {face}")
        temp = face[0][0]  # Top Left Corner

        # Top Left -> Top Right -> Bottom Right -> Bottom Left
        face[0][0] = face[2][0]  # Top Left -> Bottom Left
        face[2][0] = face[2][2]  # Top Right -> Top Left
        face[2][2] = face[0][2]  # Bottom Right -> Top Right
        face[0][2] = temp  # Bottom Left -> Bottom Right

        # Rotating Edges
        temp = face[0][1]  # Top Middle

        #  Top -> Right -> Bottom -> Left
        face[0][1] = face[1][0]  # Left -> Top
        face[1][0] = face[2][1]  # Top -> Right
        face[2][1] = face[1][2]  # Right -> Bottom
        face[1][0] = temp  # Bottom -> Left

        # print(f"After Rotating Edges: {face}")

    def __move_back(self):
        self.rotation_clockwise(self.faces['B'])
        # self.print_cube_layout()

    def __move_down(self):
        self.rotation_clockwise(self.faces['D'])

    def __move_front(self):
        self.rotation_clockwise(self.faces['F'])
        # self.print_cube_layout()

    def __move_left(self):
        self.rotation_clockwise(self.faces['L'])
        # self.print_cube_layout()

    def __move_right(self):
        self.rotation_clockwise(self.faces['R'])
        # self.print_cube_layout()

    def __move_up(self):
        self.rotation_clockwise(self.faces['U'])
        # self.print_cube_layout()

    def print_cube_layout(self):
        layout = ""
        # Top face
        layout += "       " + " ".join(self.faces['U'][0]) + "\n"
        layout += "       " + " ".join(self.faces['U'][1]) + "\n"
        layout += "       " + " ".join(self.faces['U'][2]) + "\n\n"
        # Middle faces (Left, Front, Right, Back)
        for i in range(3):
            layout += " ".join(self.faces['L'][i]) + "  "  # Left
            layout += " ".join(self.faces['F'][i]) + "  "  # Front
            layout += " ".join(self.faces['R'][i]) + "  "  # Right
            layout += " ".join(self.faces['B'][i]) + "\n"  # Back
        layout += "\n"
        # Bottom face
        layout += "       " + " ".join(self.faces['D'][0]) + "\n"
        layout += "       " + " ".join(self.faces['D'][1]) + "\n"
        layout += "       " + " ".join(self.faces['D'][2]) + "\n"
        print(layout)


def main(args):
    if (len(args) == 2):  # Checks for number of arguments
        infile = open(args[1])
    else:
        raise FileExistsError("No file given")
    contents = infile.readline()
    da_cube = contents
    # print(f"Faces of Cube: {da_cube}")
    infile.readline()  # Reads past blank line
    c = Cube()
    c.set_cube(da_cube)
    c.print_cube_layout()
    moves = []
    for line in infile:
        moves.append(line.strip())
        if moves[0].endswith("'"):
            print("Counter")
            c.rotation = False
        else:
            print("Clockwise")
            c.rotation = True
    # while moves:
    #    if (moves[0].endswith("''")):
    #        print("Counter")
    #        c.rotation = False
    #    else:
    #        c.rotation = True
        c.move(moves[0][0], c.rotation)
        c.print_cube_layout()
        moves.pop(0)
    pass


if '__main__' == __name__:
    import sys
    main(sys.argv)
