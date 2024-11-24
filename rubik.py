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
        match face:
            case 'U':
                self.affected = [
                    [self.faces['B'][2][0], self.faces['B'][2][1], self.faces['B'][2][2]],
                    [self.faces['R'][0][0], self.faces['R'][1][0], self.faces['R'][2][0]],
                    [self.faces['F'][0][0], self.faces['F'][0][1], self.faces['F'][0][2]],
                    [self.faces['L'][0][2], self.faces['L'][1][2], self.faces['L'][2][2]],
                ]
                self.labels = ['B', 'R', 'F', 'L']
                self.__move_up()
            case 'L':
                self.affected = [
                    [self.faces['U'][2][0], self.faces['U'][2][1], self.faces['U'][2][2]],
                    [self.faces['F'][0][0], self.faces['F'][1][0], self.faces['F'][2][0]],
                    [self.faces['D'][0][0], self.faces['D'][0][1], self.faces['D'][0][2]],
                    [self.faces['B'][0][2], self.faces['B'][1][2], self.faces['B'][2][2]],
                ]
                self.labels = ['U', 'F', 'D', 'B']
                self.__move_left()
            case 'F':
                self.affected = [
                    [self.faces['U'][2][0], self.faces['U'][2][1], self.faces['U'][2][2]],
                    [self.faces['R'][0][0], self.faces['R'][1][0], self.faces['R'][2][0]],
                    [self.faces['D'][0][0], self.faces['D'][0][1], self.faces['D'][0][2]],
                    [self.faces['L'][0][2], self.faces['L'][1][2], self.faces['L'][2][2]], 
                ]
                self.labels = ['U', 'R', 'D', 'L']
                self.__move_front()
            case 'R':
                self.affected = [
                    [self.faces['U'][2][0], self.faces['U'][2][1], self.faces['U'][2][2]],
                    [self.faces['B'][0][0], self.faces['B'][1][0], self.faces['B'][2][0]],
                    [self.faces['D'][0][0], self.faces['D'][0][1], self.faces['D'][0][2]],
                    [self.faces['F'][0][2], self.faces['F'][1][2], self.faces['F'][2][2]],
                ]
                self.labels = ['U', 'B', 'D', 'F']
                self.__move_right()
            case 'B':
                self.affected = [
                    [self.faces['U'][2][0], self.faces['U'][2][1], self.faces['U'][2][2]],
                    [self.faces['L'][0][0], self.faces['L'][1][0], self.faces['L'][2][0]],
                    [self.faces['D'][0][0], self.faces['D'][0][1], self.faces['D'][0][2]],
                    [self.faces['R'][0][2], self.faces['R'][1][2], self.faces['R'][2][2]],
                ]
                self.labels = ['U', 'L', 'D', 'R']
                self.__move_back()
            case 'D':
                self.affected = [
                    [self.faces['F'][2][0], self.faces['F'][2][1], self.faces['F'][2][2]],
                    [self.faces['R'][0][0], self.faces['R'][1][0], self.faces['R'][2][0]],
                    [self.faces['B'][0][0], self.faces['B'][0][1], self.faces['B'][0][2]],
                    [self.faces['L'][0][2], self.faces['L'][1][2], self.faces['L'][2][2]],
                ]
                self.labels = ['F', 'R', 'B', 'L']
                self.__move_down()
            case _:
                raise ValueError(f"{face} is not a face")
        # print(f"affected: {self.affected}")

    def rotation_clockwise(self, face):
        # Rotate Corners
        # print(f"face: {face}")
        temp_tl = face[0][0]  # Top Left Corner
        temp_tr = face[0][2]  # Top Right Corner
        temp_bl = face[2][0]  # Bottom Left Corner
        temp_br = face[2][2]  # Bottom Right Corner

        # Top Left -> Top Right -> Bottom Right -> Bottom Left
        face[0][0] = temp_bl  # Top Left -> Bottom Left
        face[0][2] = temp_tl  # Top Right -> Top Left
        face[2][2] = temp_tr  # Bottom Right -> Top Right
        face[2][0] = temp_br  # Bottom Left -> Bottom Right

        # print(f"After roating corner:{face}")

        # Rotating Edges
        temp_t = face[0][1]  # Top Middle
        temp_l = face[1][0]  # Left Middle
        temp_b = face[2][1]  # Bottom Middle
        temp_r = face[1][2]  # Right Middle

        #  Top -> Right -> Bottom -> Left
        face[0][1] = temp_l  # Left -> Top
        face[1][2] = temp_t  # Top -> Right
        face[2][1] = temp_r  # Right -> Bottom
        face[1][0] = temp_b  # Bottom -> Left

        # print(f"After Rotating Edges: {face}")

        self.clockwise_aftermath(face)

    def rotation_counterclockwise(self, face):
        self.rotation_clockwise(face)
        self.counterclockwise_aftermath(face)
        self.counterclockwise_aftermath(face)
        self.rotation_clockwise(face)
        self.counterclockwise_aftermath(face)
        self.counterclockwise_aftermath(face)
        self.rotation_clockwise(face)
        self.counterclockwise_aftermath(face)
        self.counterclockwise_aftermath(face)

    def clockwise_aftermath(self, face):
        face = face
        # print(f"affected: {self.affected}")
        # print(f"HHHHHHHHHHHHHHHHHHHHHHHHHHh: {self.affected[0]}")

        # Part 1
        temp_t = self.affected[0][0]
        temp_r = self.affected[1][0]
        temp_b = self.affected[2][2]
        temp_l = self.affected[3][2]

        # Top -> Right -> Bottom -> Left
        self.affected[0][0] = temp_l
        self.affected[1][0] = temp_t
        self.affected[2][2] = temp_r
        self.affected[3][2] = temp_b

        # Affect the Cube
        self.faces[self.labels[0]][2][0] = self.affected[0][0]  # Updating Left on Top
        self.faces[self.labels[1]][0][0] = self.affected[1][0]  # Updating Top on Right
        self.faces[self.labels[2]][0][2] = self.affected[2][2]  # Updating Left on Bottom
        self.faces[self.labels[3]][2][2] = self.affected[3][2]  # Updating Bottom on Left

        # Part 2
        temp_t = self.affected[0][1]
        temp_r = self.affected[1][1]
        temp_b = self.affected[2][1]
        temp_l = self.affected[3][1]

        # Top -> Right -> Bottom -> Left
        self.affected[0][1] = temp_l
        self.affected[1][1] = temp_t
        self.affected[2][1] = temp_r
        self.affected[3][1] = temp_b

        # Update the Cube
        self.faces[self.labels[0]][2][1] = self.affected[0][1]  # Updating Middle on Top
        self.faces[self.labels[1]][1][0] = self.affected[1][1]  # Updating Middle on Right
        self.faces[self.labels[2]][0][1] = self.affected[2][1]  # Updating Middle on Bottom
        self.faces[self.labels[3]][1][2] = self.affected[3][1]  # Updating Middle on Left

        # Part 3
        temp_t = self.affected[0][2]
        temp_r = self.affected[1][2]
        temp_b = self.affected[2][0]
        temp_l = self.affected[3][0]

        # Top -> Right -> Bottom -> Left
        self.affected[0][2] = temp_l
        self.affected[1][2] = temp_t
        self.affected[2][0] = temp_r
        self.affected[3][0] = temp_b

        # Update the Cube
        self.faces[self.labels[0]][2][2] = self.affected[0][2]  # Updating Right on Top
        self.faces[self.labels[1]][2][0] = self.affected[1][2]  # Updating Bottom on Right
        self.faces[self.labels[2]][0][0] = self.affected[2][0]  # Updating Left on Bottom
        self.faces[self.labels[3]][0][2] = self.affected[3][0]  # Updating Top on Left

    def counterclockwise_aftermath(self, face):
        self.clockwise_aftermath(face)
        self.clockwise_aftermath(face)
        self.clockwise_aftermath(face)

    def __move_back(self):
        if self.rotation:
            self.rotation_clockwise(self.faces['B'])
        else:
            self.rotation_counterclockwise(self.faces['B'])

    def __move_down(self):
        if self.rotation:
            self.rotation_clockwise(self.faces['D'])
        else:
            self.rotation_counterclockwise(self.faces['D'])

    def __move_front(self):
        if self.rotation:
            self.rotation_clockwise(self.faces['F'])
        else:
            self.rotation_counterclockwise(self.faces['F'])

    def __move_left(self):
        if self.rotation:
            self.rotation_clockwise(self.faces['L'])
        else:
            self.rotation_counterclockwise(self.faces['L'])
            
    def __move_right(self):
        if self.rotation:
            self.rotation_clockwise(self.faces['R'])
        else:
            self.rotation_counterclockwise(self.faces['R'])

    def __move_up(self):
        if self.rotation:
            self.rotation_clockwise(self.faces['U'])
        else:
            self.rotation_counterclockwise(self.faces['U'])

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
    moves = []
    for line in infile:
        moves.append(line.strip())
    c = Cube()
    c.set_cube(da_cube)
    c.print_cube_layout()
    while moves:
        if (moves[0].endswith("''")):
            c.rotation = False
        else:
            c.rotation = True

        c.move(moves[0], c.rotation)
        c.print_cube_layout()
        moves.pop(0)
    pass


if '__main__' == __name__:
    import sys
    main(sys.argv)
