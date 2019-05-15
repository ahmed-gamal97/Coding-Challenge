import unittest
import solution as sl


class TestAlgorithm(unittest.TestCase):
    def test_keep_Alphabet(self):
        self.assertEqual(sl.keep_Alphabet('ahsmeda2'), 'ahsmeda')
        self.assertEqual(sl.keep_Alphabet('a23me8d'), 'amed')

    def test_convert_to_lowercase(self):
        self.assertEqual(sl.convert_to_lowercase('Ahmed Gamal'), 'ahmed gamal')
        self.assertEqual(sl.convert_to_lowercase('HelloHello'), 'hellohello')

    def test_clean_string(self):
        self.assertEqual(sl.clean_string('Ahmed Gamal'), 'aa')
        self.assertEqual(sl.clean_string('abcDabcB'), 'abcabc')

    def test_convert_to_third(self):
        self.assertEqual(sl.convert_to_third('a', 'c'), 'b')
        self.assertEqual(sl.convert_to_third('c', 'a'), 'b')
        self.assertEqual(sl.convert_to_third('b', 'a'), 'c')
        self.assertEqual(sl.convert_to_third('c', 'b'), 'a')

    def test_find_possible_positions(self):
        self.assertEqual(sl.find_possible_positions('abbc'), [0, 2])
        self.assertEqual(sl.find_possible_positions('bcab'), [0, 1, 2])

    def test_replace(self):
        self.assertEqual(sl.replace('abbc', 0), 'cbc')
        self.assertEqual(sl.replace('abbc', 2), 'aba')

    def test_keep_distinct(self):
        self.assertEqual(sl.keep_distinct(['aa','bb', 'aa']), ['aa', 'bb'])

    def test_keep_minimum(self):
        self.assertEqual(sl.keep_minimum(['aa', 'bb', 'aaaaa', 'cc']), ['aa', 'bb', 'cc'])

    def test_shortening_string(self):
        self.assertEqual(sl.shortening_string('aba'), ['b'])
        self.assertEqual(sl.shortening_string('aa'), ['aa'])
        self.assertEqual(sl.shortening_string('cab'), ['bb', 'cc'])
        self.assertEqual(sl.shortening_string('bcab'), ['b'])
        self.assertEqual(sl.shortening_string('abcc'), ['c'])


if __name__ == '__main__':
    unittest.main()