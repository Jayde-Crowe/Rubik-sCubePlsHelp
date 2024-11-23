import collections
import itertools
from unittest import mock

import pytest

import rubik


def _check_cube(cube, colors):
    for f, face in colors.items():  # face -> [[row], [row], [row]]
        for i, row in enumerate(face, start=1):
            for j, color in enumerate(row, start=1):
                assert cube.get_color_at(f, i, j) == color, \
                    f"Incorrect color at ({f}, {i}, {j}):\n{cube}"


@pytest.mark.unit
class TestCube:
    def test_get_color_at(self):
        cube = rubik.Cube()
        _check_cube(cube, dict(zip('ULFRBD', 'WGRBOY')))

        colors = {
            'U': [['G', 'W', 'B'], ['Y', 'W', 'R'], ['Y', 'O', 'R']],  # up
            'L': [['Y', 'R', 'B'], ['O', 'O', 'O'], ['O', 'Y', 'O']],  # left
            'F': [['R', 'G', 'W'], ['W', 'G', 'G'], ['W', 'B', 'R']],  # front
            'R': [['G', 'G', 'O'], ['W', 'R', 'W'], ['Y', 'R', 'W']],  # right
            'B': [['W', 'R', 'O'], ['B', 'B', 'B'], ['B', 'Y', 'B']],  # back
            'D': [['G', 'Y', 'G'], ['O', 'Y', 'B'], ['Y', 'G', 'R']],  # down
        }
        cube = rubik.Cube("".join(
            [col for face in colors.values() for row in face for col in row]))
        _check_cube(cube, colors)

    def test_get_color_at_1_based_indexing(self):
        cube = rubik.Cube()
        for row, column in itertools.product([0, 4], [0, 4]):
            with pytest.raises(IndexError):
                for face in 'ULFRBD':
                    cube.get_color_at(face, row, column)

    def test_get_color_at_invalid_face(self):
        cube = rubik.Cube()
        for face in 'XYZxyz123':
            with pytest.raises(ValueError):
                cube.get_color_at(face, 1, 3)

    def test_move(self):
        cube = rubik.Cube()
        for face, method in {
            'B': '_move_back',
            'D': '_move_down',
            'F': '_move_front',
            'L': '_move_left',
            'R': '_move_right',
            'U': '_move_up',
        }.items():
            with mock.patch.object(cube, method) as mock__move_method:
                cube.move(face, True)
                mock__move_method.assert_called_once_with()

                cube.move(face, False)
                mock__move_method.assert_has_calls(
                    [mock.call(), mock.call(), mock.call()])

    def test__move_back_clockwise(self):
        cube = rubik.Cube()
        cube.move('B', True)

        _check_cube(cube, {
            'U': [['B', 'B', 'B'], ['W', 'W', 'W'], ['W', 'W', 'W']],  # up
            'L': [['W', 'G', 'G'], ['W', 'G', 'G'], ['W', 'G', 'G']],  # left
            'F': [['R', 'R', 'R'], ['R', 'R', 'R'], ['R', 'R', 'R']],  # front
            'R': [['B', 'B', 'Y'], ['B', 'B', 'Y'], ['B', 'B', 'Y']],  # right
            'B': [['O', 'O', 'O'], ['O', 'O', 'O'], ['O', 'O', 'O']],  # back
            'D': [['Y', 'Y', 'Y'], ['Y', 'Y', 'Y'], ['G', 'G', 'G']],  # down
        })

    def test__move_back_counterclockwise(self):
        cube = rubik.Cube()
        cube.move('B', False)

        _check_cube(cube, {
            'U': [['G', 'G', 'G'], ['W', 'W', 'W'], ['W', 'W', 'W']],  # up
            'L': [['Y', 'G', 'G'], ['Y', 'G', 'G'], ['Y', 'G', 'G']],  # left
            'F': [['R', 'R', 'R'], ['R', 'R', 'R'], ['R', 'R', 'R']],  # front
            'R': [['B', 'B', 'W'], ['B', 'B', 'W'], ['B', 'B', 'W']],  # right
            'B': [['O', 'O', 'O'], ['O', 'O', 'O'], ['O', 'O', 'O']],  # back
            'D': [['Y', 'Y', 'Y'], ['Y', 'Y', 'Y'], ['B', 'B', 'B']],  # down
        })

    def test__move_down_clockwise(self):
        cube = rubik.Cube()
        cube.move('D', True)

        _check_cube(cube, {
            'U': [['W', 'W', 'W'], ['W', 'W', 'W'], ['W', 'W', 'W']],  # up
            'L': [['G', 'G', 'G'], ['G', 'G', 'G'], ['O', 'O', 'O']],  # left
            'F': [['R', 'R', 'R'], ['R', 'R', 'R'], ['G', 'G', 'G']],  # front
            'R': [['B', 'B', 'B'], ['B', 'B', 'B'], ['R', 'R', 'R']],  # right
            'B': [['O', 'O', 'O'], ['O', 'O', 'O'], ['B', 'B', 'B']],  # back
            'D': [['Y', 'Y', 'Y'], ['Y', 'Y', 'Y'], ['Y', 'Y', 'Y']],  # down
        })

    def test__move_down_counterclockwise(self):
        cube = rubik.Cube()
        cube.move('D', False)

        _check_cube(cube, {
            'U': [['W', 'W', 'W'], ['W', 'W', 'W'], ['W', 'W', 'W']],  # up
            'L': [['G', 'G', 'G'], ['G', 'G', 'G'], ['R', 'R', 'R']],  # left
            'F': [['R', 'R', 'R'], ['R', 'R', 'R'], ['B', 'B', 'B']],  # front
            'R': [['B', 'B', 'B'], ['B', 'B', 'B'], ['O', 'O', 'O']],  # right
            'B': [['O', 'O', 'O'], ['O', 'O', 'O'], ['G', 'G', 'G']],  # back
            'D': [['Y', 'Y', 'Y'], ['Y', 'Y', 'Y'], ['Y', 'Y', 'Y']],  # down
        })

    def test__move_front_clockwise(self):
        cube = rubik.Cube()
        cube.move('F', True)

        _check_cube(cube, {
            'U': [['W', 'W', 'W'], ['W', 'W', 'W'], ['G', 'G', 'G']],  # up
            'L': [['G', 'G', 'Y'], ['G', 'G', 'Y'], ['G', 'G', 'Y']],  # left
            'F': [['R', 'R', 'R'], ['R', 'R', 'R'], ['R', 'R', 'R']],  # front
            'R': [['W', 'B', 'B'], ['W', 'B', 'B'], ['W', 'B', 'B']],  # right
            'B': [['O', 'O', 'O'], ['O', 'O', 'O'], ['O', 'O', 'O']],  # back
            'D': [['B', 'B', 'B'], ['Y', 'Y', 'Y'], ['Y', 'Y', 'Y']],  # down
        })

    def test__move_front_counterclockwise(self):
        cube = rubik.Cube()
        cube.move('F', False)

        _check_cube(cube, {
            'U': [['W', 'W', 'W'], ['W', 'W', 'W'], ['B', 'B', 'B']],  # up
            'L': [['G', 'G', 'W'], ['G', 'G', 'W'], ['G', 'G', 'W']],  # left
            'F': [['R', 'R', 'R'], ['R', 'R', 'R'], ['R', 'R', 'R']],  # front
            'R': [['Y', 'B', 'B'], ['Y', 'B', 'B'], ['Y', 'B', 'B']],  # right
            'B': [['O', 'O', 'O'], ['O', 'O', 'O'], ['O', 'O', 'O']],  # back
            'D': [['G', 'G', 'G'], ['Y', 'Y', 'Y'], ['Y', 'Y', 'Y']],  # down
        })

    def test__move_left_clockwise(self):
        cube = rubik.Cube()
        cube.move('L', True)

        _check_cube(cube, {
            'U': [['O', 'W', 'W'], ['O', 'W', 'W'], ['O', 'W', 'W']],  # up
            'L': [['G', 'G', 'G'], ['G', 'G', 'G'], ['G', 'G', 'G']],  # left
            'F': [['W', 'R', 'R'], ['W', 'R', 'R'], ['W', 'R', 'R']],  # front
            'R': [['B', 'B', 'B'], ['B', 'B', 'B'], ['B', 'B', 'B']],  # right
            'B': [['O', 'O', 'Y'], ['O', 'O', 'Y'], ['O', 'O', 'Y']],  # back
            'D': [['R', 'Y', 'Y'], ['R', 'Y', 'Y'], ['R', 'Y', 'Y']],  # down
        })

    def test__move_left_counterclockwise(self):
        cube = rubik.Cube()
        cube.move('L', False)

        _check_cube(cube, {
            'U': [['R', 'W', 'W'], ['R', 'W', 'W'], ['R', 'W', 'W']],  # up
            'L': [['G', 'G', 'G'], ['G', 'G', 'G'], ['G', 'G', 'G']],  # left
            'F': [['Y', 'R', 'R'], ['Y', 'R', 'R'], ['Y', 'R', 'R']],  # front
            'R': [['B', 'B', 'B'], ['B', 'B', 'B'], ['B', 'B', 'B']],  # right
            'B': [['O', 'O', 'W'], ['O', 'O', 'W'], ['O', 'O', 'W']],  # back
            'D': [['O', 'Y', 'Y'], ['O', 'Y', 'Y'], ['O', 'Y', 'Y']],  # down
        })

    def test__move_right_clockwise(self):
        cube = rubik.Cube()
        cube.move('R', True)

        _check_cube(cube, {
            'U': [['W', 'W', 'R'], ['W', 'W', 'R'], ['W', 'W', 'R']],  # up
            'L': [['G', 'G', 'G'], ['G', 'G', 'G'], ['G', 'G', 'G']],  # left
            'F': [['R', 'R', 'Y'], ['R', 'R', 'Y'], ['R', 'R', 'Y']],  # front
            'R': [['B', 'B', 'B'], ['B', 'B', 'B'], ['B', 'B', 'B']],  # right
            'B': [['W', 'O', 'O'], ['W', 'O', 'O'], ['W', 'O', 'O']],  # back
            'D': [['Y', 'Y', 'O'], ['Y', 'Y', 'O'], ['Y', 'Y', 'O']],  # down
        })

    def test__move_right_counterclockwise(self):
        cube = rubik.Cube()
        cube.move('R', False)

        _check_cube(cube, {
            'U': [['W', 'W', 'O'], ['W', 'W', 'O'], ['W', 'W', 'O']],  # up
            'L': [['G', 'G', 'G'], ['G', 'G', 'G'], ['G', 'G', 'G']],  # left
            'F': [['R', 'R', 'W'], ['R', 'R', 'W'], ['R', 'R', 'W']],  # front
            'R': [['B', 'B', 'B'], ['B', 'B', 'B'], ['B', 'B', 'B']],  # right
            'B': [['Y', 'O', 'O'], ['Y', 'O', 'O'], ['Y', 'O', 'O']],  # back
            'D': [['Y', 'Y', 'R'], ['Y', 'Y', 'R'], ['Y', 'Y', 'R']],  # down
        })

    def test__move_up_clockwise(self):
        cube = rubik.Cube()
        cube.move('U', True)

        _check_cube(cube, {
            'U': [['W', 'W', 'W'], ['W', 'W', 'W'], ['W', 'W', 'W']],  # up
            'L': [['R', 'R', 'R'], ['G', 'G', 'G'], ['G', 'G', 'G']],  # left
            'F': [['B', 'B', 'B'], ['R', 'R', 'R'], ['R', 'R', 'R']],  # front
            'R': [['O', 'O', 'O'], ['B', 'B', 'B'], ['B', 'B', 'B']],  # right
            'B': [['G', 'G', 'G'], ['O', 'O', 'O'], ['O', 'O', 'O']],  # back
            'D': [['Y', 'Y', 'Y'], ['Y', 'Y', 'Y'], ['Y', 'Y', 'Y']],  # down
        })

    def test__move_up_counterclockwise(self):
        cube = rubik.Cube()
        cube.move('U', False)

        _check_cube(cube, {
            'U': [['W', 'W', 'W'], ['W', 'W', 'W'], ['W', 'W', 'W']],  # up
            'L': [['O', 'O', 'O'], ['G', 'G', 'G'], ['G', 'G', 'G']],  # left
            'F': [['G', 'G', 'G'], ['R', 'R', 'R'], ['R', 'R', 'R']],  # front
            'R': [['R', 'R', 'R'], ['B', 'B', 'B'], ['B', 'B', 'B']],  # right
            'B': [['B', 'B', 'B'], ['O', 'O', 'O'], ['O', 'O', 'O']],  # back
            'D': [['Y', 'Y', 'Y'], ['Y', 'Y', 'Y'], ['Y', 'Y', 'Y']],  # down
        })


@pytest.mark.integration
@mock.patch('builtins.print')
@mock.patch.object(rubik.Cube, 'move')
def test_main(mock_move, mock_print):
    contents = """
WWWWWWWWW GGGGGGGGG RRRRRRRRR BBBBBBBBB OOOOOOOOO YYYYYYYYY

F
F'
R
R'
U
U'
B
B'
L
L'
D
D'
""".strip()
    with mock.patch('builtins.open',
                    mock.mock_open(read_data=contents)) as mock_open:
        rubik.main(['rubik.py', 'fake-path'])
        assert mock_open.call_count == 1, "Missing expected open(...) call"
        assert 'fake-path' in [args for args in mock_open.call_args.args], \
            "Missing expected path in open(...) call"

    calls = []
    for move, clockwise in itertools.product('FRUBLD', [True, False]):
        calls.append(mock.call(move, clockwise=clockwise))

    mock_move.assert_has_calls(calls, any_order=False)
    mock_print.assert_called()  # should be called with cube as argument


@pytest.mark.integration
@pytest.mark.parametrize("configuration,moves", [
    ("GWOGWORRY WWBYGRYGG WWBGRBOYY RWWYBOGBO BBRYOGYOG WRROYROBB",
     "F,R,U,B,L,D".split(',')),
    ("YBBGWWGRR GWWGGROOB OWWGRYYYB GOOBBYRRY WWROOYBBY RRWGYBGOO",
     "D',L',B',U',R',F'".split(',')),
    ("ROOOBRRBW WYGWYRBBB YWOGOGOGR GBYOWYGOB GWBRRRWGR YYWYGBYWO",
     "U',D',B',U',R',U,R,R,L',B',U,U,D,D,F',L,L,F,F,U,U,R,R,B,B,"
     "U,U,R,R,D".split(',')),
    ("WRBYRBWWG RGBGGOYWG OBYYYRYBW RORGBRGRW YBGYWOBGO OYOOOWBWR",
     "B,D,L,L,U',R,B,B,L,L,D,F',B,L',F',D',L,L,B,B,R,R,L,L,D,D,L,"
     "L".split(',')),
    ("BYWOYYYRW OGRYGRBWO GWBBOGGBY OGOWBYROG GRYBROWGW YOBBWWRRR",
     "U',R,U',L,L,B,L',U,D,B,U,B,B,U,U,R',L,U,U,B,B,L,L,D,F,F,D,"
     "D".split(',')),
    ])
def test_moves(configuration, moves):
    cube = rubik.Cube(configuration)
    for move in moves:
        assert len(move) <= 2, "Invalid move: {move}"
        cube.move(move[0], not move.endswith("'"))

    faces = {}
    for face in 'ULFRBD':
        colors = []
        for i in range(3):
            for j in range(3):
                colors.append(cube.get_color_at(face, i + 1, j + 1))

        # ensure face has a single color
        colors = collections.Counter(colors)
        assert len(colors) == 1, f"{face} face is not solved:\n{cube}"

        faces[face] = next(iter(colors.keys()))  # only one color on face

    # ensure all colors present (one on each face)
    assert len(faces) == 6  # all faces present
    colors = collections.Counter(faces.values())
    assert len(colors) == 6, f"Incorrect number of colors on faces:\n{cube}"


# support running this file directly (e.g., within an IDE)
if '__main__' == __name__:
    pytest.main()
