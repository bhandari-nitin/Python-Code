##########################
##### Rotate Matrix ######
##########################
import unittest

def rotateMatrix(matrix):
    rows = len(matrix)
    columns = len(matrix[0])
    size_matrix = rows
    # Layers that need to be  rotated within a matrix   
    rotate_layers = size_matrix // 2
    for layer in range(0, rotate_layers):
        first = layer
        last = size_matrix - first - 1
        for element in (first, last):
            offset = element - first
            top = matrix[first][element]
            right_side = matrix[element][last]
            bottom = matrix[last][last-offset]
            left_side = matrix[last-offset][first]

            matrix[first][element] = left_side
            matrix[element][last] = top
            matrix[last][last-offset] = right_side
            matrix[last-offset][first] = bottom
    return matrix

class Test(unittest.TestCase):
    data = [
        ([
            [1, 2, 3, 4, 5],
            [6, 7, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 17, 18, 19, 20],
            [21, 22, 23, 24, 25]
        ], [
            [21, 16, 11, 6, 1],
            [22, 17, 12, 7, 2],
            [23, 18, 13, 8, 3],
            [24, 19, 14, 9, 4],
            [25, 20, 15, 10, 5]
        ])
    ]
    
    def test_rotate_matrix(self):
        for [test_matrix, expected] in self.data:
            actual = rotateMatrix(test_matrix)
            print actual
            self.assertEqual(actual, expected)
        
if __name__ == '__main__':
    unittest.main()
