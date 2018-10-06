import unittest

# runtime : O(|s|)
def urlify(s):
    for i in range(0, len(s)):
        if s[i] == ' ':
            s = s[:i] + '%20' + s[i+1:]
    return s

def urlify2(s):
    return s.replace(' ', '%20',)

class Test(unittest.TestCase):
    strings = ['A B', 'AB', ' bb ']

    def urltest(self):
        # True
        for string in self.strings:
            actual = urlify(string)
            self.assertTrue(actual)

if __name__ == '__main__':
    unittest.main()
