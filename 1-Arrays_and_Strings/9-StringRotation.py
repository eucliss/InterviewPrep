import unittest


# Not optimized or using the isSubstring()
# Runtime : O(|s1|)
def StringRotation(s1, s2):
    if len(s1) != len(s2):
        return False
    elif ''.join(set(s1)) != ''.join(set(s2)):
        return False
    elif s1 == s2:
        return True
    else:
        for i in range(0,len(s1)):
            if s1[i:] + s1[:i] == s2:
                return True
        return False

class Test(unittest.TestCase):
    T = [('ab', 'ba'), ('hey', 'eyh'), ('coding', 'dingco'), ('abbaabba', 'baabbaab')]
    F = [('ab', 'abc'), ('abc', 'cvd'), ('abba', 'baba'), ('coding', 'dingoc')]

    def test_rotate(self):
        # True
        for (s1,s2) in self.T:
            actual = StringRotation(s1,s2)
            self.assertTrue(actual)
        # False
        for (s1,s2) in self.F:
            actual = StringRotation(s1,s2)
            self.assertFalse(actual)


if __name__ == '__main__':
    unittest.main()
