
import unittest

# Runtime : O(|s1|)
def check_permutation(s1, s2):
    if len(s1) != len(s2):
        return False
    for i in s1:
        if s2 == s2.replace(i, '', 1):
            return False
    return True

class Test(unittest.TestCase):
    T = [('', ''), ('aba', 'baa'), ('abcd', 'bcda'), ('abbb', 'bbab'), ('abcd', 'bacd'), ('3563476', '7334566'), ('wef34f', 'wffe34')]
    F = [('aba', 'ab'), ('abcd', 'abc '), ('abcc', 'ccbb'),('abcd', 'd2cba'), ('2354', '1234'), ('dcw4f', 'dcw5f'),]

    def test_permutation(self):
        # True
        for (s1,s2) in self.T:
            actual = check_permutation(s1,s2)
            self.assertTrue(actual)
        # False
        for (s1,s2) in self.F:
            actual = check_permutation(s1,s2)
            self.assertFalse(actual)


if __name__ == '__main__':
    unittest.main()
