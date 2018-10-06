import unittest

# Runtime : O(n)
def is_unique(s):
    if len(s) == 1 or len(s) == 0:
        return True
    else:
        ht = {}
        for i in s:
            if i in ht:
                return False
            else:
                ht[i] = True
        return True

# Without using a datastructure
# Runtime : O(n^2)
def is_unique2(s):
    for i in range(0,len(s)):
        for j in range(0,len(s)):
            if j == i:
                continue
            else:
                if s[i] == s[j]:
                    return False
    return True

class Test(unittest.TestCase):
    dataT = [('abcd'), ('s4fad'), (''), ('a')]
    dataF = [('23ds2'), ('hb 627jh=j ()'), ('abba')]

    def test_unique(self):
        # true check
        for test_string in self.dataT:
            actual = is_unique(test_string)
            self.assertTrue(actual)
        # false check
        for test_string in self.dataF:
            actual = is_unique(test_string)
            self.assertFalse(actual)

        # Unique 2 tests
        for test_string in self.dataT:
            actual = is_unique2(test_string)
            self.assertTrue(actual)
        # false check
        for test_string in self.dataF:
            actual = is_unique2(test_string)
            self.assertFalse(actual)


if __name__ == '__main__':
    unittest.main()
