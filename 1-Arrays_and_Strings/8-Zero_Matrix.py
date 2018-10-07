import unittest


# Runtime: O(MxN)
def ZeroMatrix(M):
    indexes = []
    for i in range(0, len(M)):
        zeroes = M[i].count(0)
        if zeroes == 1:
            indexes.append((i, M[i].index(0)))
        if zeroes >= 2:
            for j in range(0, len(M[i])):
                if M[i][j] == 0:
                    indexes.append((i,j))
    for (row, col) in indexes:
        for i in range(0, len(M[row])):
            M[row][i] = 0
        for row_index in range(0, len(M)):
            M[row_index][col] = 0
    return M


class Test(unittest.TestCase):
    data = [
        ([
            [1, 2, 3, 4, 0],
            [6, 0, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 0, 18, 19, 20],
            [21, 22, 23, 24, 25]
            ], [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [11, 0, 13, 14, 0],
            [0, 0, 0, 0, 0],
            [21, 0, 23, 24, 0]
            ]),
            ([
            [1, 2, 3, 4, 3],
            [6, 3, 0, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 0, 18, 19, 20],
            [21, 22, 23, 24, 0]
            ], [
            [1, 0, 0, 4, 0],
            [0, 0, 0, 0, 0],
            [11, 0, 0, 14, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0]
            ])
            ]

    def test_zero_matrix(self):
        for [test_matrix, expected] in self.data:
            actual = ZeroMatrix(test_matrix)
            self.assertEqual(actual, expected)



if __name__ == '__main__':
    # print(ZeroMatrix([[0,2,3,4],[5,0,7,8],[8,9,10,11]]))
    unittest.main()
