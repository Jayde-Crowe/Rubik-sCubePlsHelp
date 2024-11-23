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

    def set_cube(self, string):
        data = string.split()
        print(data)
        if len(data) != 6:
            raise ValueError(f"Six != {len(data)}")
        for element in data:
            if len(element) != 9:
                raise ValueError(f"Nine != {len(element)}")
        for f in range(6):
            index = 0
            for x in range(3):
                for y in range(3):
                    self.faces[list(self.list.keys())[f]][x][y] = data[f][index]
                    index = index + 1

    def move(self, face, rotation):
        self.affected = []
        i = 0
        match face:
            case 'U':
                face_w = self.faces['U']
                self.affected = [
                    [self.faces['B'][2][0], self.faces['B'][2][1], self.faces['B'][2][2]],
                    [self.faces['R'][0][0], self.faces['R'][1][0], self.faces['R'][2][0]],
                    [self.faces['F'][0][0], self.faces['F'][0][1], self.faces['F'][0][2]],
                    [self.faces['L'][0][2], self.faces['L'][1][2], self.faces['L'][2][2]],
                ]
            case 'L':
                face_w = self.faces['L']
                self.affected = [
                    self.faces['U'][2],
                    [row[2] for row in self.faces['F']],
                    self.faces['D'][0],
                    [row[0] for row in self.faces['B']]
                ]
            case 'F':
                face_w = self.faces['F']
                self.affected = [
                    self.faces['U'][2],
                    [row[2] for row in self.faces['R']],
                    self.faces['D'][0],
                    [row[0] for row in self.faces['L']]
                ]
            case 'R':
                face_w = self.faces['R']
                self.affected = [
                    self.faces['U'][2],
                    [row[2] for row in self.faces['B']],
                    self.faces['D'][0],
                    [row[0] for row in self.faces['F']]
                ]
            case 'B':
                face_w = self.faces['B']
                self.affected = [
                    self.faces['U'][2],
                    [row[2] for row in self.faces['L']],
                    self.faces['D'][0],
                    [row[0] for row in self.faces['R']]
                ]
            case 'D':
                face_w = self.faces['D']
                self.affected = [
                    self.faces['F'][2],
                    [row[2] for row in self.faces['R']],
                    self.faces['B'][0],
                    [row[0] for row in self.faces['L']]
                ]
            case _:
                raise ValueError(f"{face} is not a face")
        print(f"affected: {self.affected}")
        if rotation:
            self.rotation_clockwise(face_w)
            self.clockwise_aftermath(face)
        else:
            self.rotation_counterclockwise(face_w)
            self.counterclockwise_aftermath(face)

    def rotation_clockwise(self, face):
        # Rotate Corners
        temp_tl = face[0][0]
        temp_tr = face[0][2]
        temp_bl = face[2][0]
        temp_br = face[2][2]

        face[0][0] = temp_bl
        face[0][2] = temp_tl
        face[2][2] = temp_tr
        face[2][0] = temp_br

        # Rotating Edges
        temp_t = face[0][1]
        temp_l = face[1][0]
        temp_b = face[2][1]
        temp_r = face[1][2]

        face[0][1] = temp_l
        face[1][0] = temp_b
        face[2][1] = temp_r
        face[1][2] = temp_t
    
    def rotation_counterclockwise(self, face):

        # Rotating Corners
        temp_tl = face[0][0]
        temp_tr = face[0][2]
        temp_bl = face[2][0]
        temp_br = face[2][2]

        face[0][0] = temp_tr
        face[0][2] = temp_br
        face[2][2] = temp_bl
        face[2][0] = temp_tl

        # Rotate Edges
        temp_t = face[0][1]
        temp_l = face[1][0]
        temp_b = face[2][1]
        temp_r = face[1][2]

        face[0][1] = temp_r
        face[1][0] = temp_t
        face[2][1] = temp_l
        face[1][2] = temp_b

    def clockwise_aftermath(self, face):
        print(f"affected: {self.affected}")
        # Part 1
        top = self.affected[0]
        right = self.affected[1]
        bottom = self.affected[2]
        left = self.affected[3]
        temp_l = right[0]
        temp_r = left[2]
        right[0] = bottom[2]
        left[2] = top[0]
        top[0] = temp_l
        bottom[2] = temp_r
        # Part 2
        temp_l = right[0]
        temp_r = left[2]
        right[0] = bottom[1]
        left[2] = top[1]
        top[1] = temp_l
        bottom[1] = temp_r
        # Part 3
        temp_l = right[0]
        temp_r = left[2]
        right[0] = bottom[0]
        left[2] = top[2]
        bottom[0] = temp_r
        top[2] = temp_l

    def counterclockwise_aftermath(self, face):
        self.clockwise_aftermath(face)
        self.clockwise_aftermath(face)
        self.clockwise_aftermath(face)






def main(args):
    pass


if '__main__' == __name__:
    import sys
    main(sys.argv)
