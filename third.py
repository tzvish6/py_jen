import unittest

def longest_word(file):
    with open(file, 'r') as infile:
                words = infile.read().split()
    max_len = len(max(words, key=len))
    longestWord = ([word for word in words if len(word) == max_len])
    print("Longest word is: {}. num of chars: {}".format(longestWord, len(longestWord[0])))
    return(len(longestWord[0]))

class MyTest(unittest.TestCase):
    def test(self):
        self.assertGreater(longest_word('test.txt'), 9)

if __name__ == '__main__':
    unittest.main()
