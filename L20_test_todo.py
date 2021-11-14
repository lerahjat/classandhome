import unittest
from L20_pract import SignedInt, Matrix


class TestTask(unittest.TestCase):

    def test_sing(self):
        signed_int = SignedInt(3, '+')
        signed_int1 = SignedInt(3, '-')
        self.assertEqual(signed_int.sign, '+')
        self.assertEqual(signed_int1.sign, '-')

    def test_sing_eror(self):
        with self.assertRaises(ValueError):
            signed_int = SignedInt(3, '=')

    def test_modulus(self):
        signed_int = SignedInt(3, '+')
        self.assertEqual(signed_int.modulus, 3)


    def test_modulus_eror(self):
        with self.assertRaises(ValueError):
            signed_int = SignedInt('3', '=')

    def test_str(self):
        signed_int = SignedInt(3, '+')
        signed_int1 = SignedInt(3, '-')
        self.assertEqual(str(signed_int), '3')
        self.assertEqual(str(signed_int1), '-3')

    def test_eg(self):
        signed_int = SignedInt(3, '+')
        signed_int1 = SignedInt(3, '+')
        self.assertTrue(signed_int == signed_int1)

    def test_lt(self):
        signed_int = SignedInt(3, '-')
        signed_int1 = SignedInt(3, '+')
        self.assertTrue(signed_int < signed_int1)

    def test_le(self):
        signed_int = SignedInt(3, '+')
        signed_int1 = SignedInt(3, '+')
        self.assertTrue(signed_int <= signed_int1)

    def test_gt(self):
        signed_int = SignedInt(4, '+')
        signed_int1 = SignedInt(3, '+')
        self.assertTrue(signed_int > signed_int1)

    def test_ge(self):
        signed_int = SignedInt(3, '+')
        signed_int1 = SignedInt(3, '+')
        self.assertTrue(signed_int >= signed_int1)

    def test_iter(self):
        matrix = Matrix(3)
        matrix_iter = iter(matrix)
        self.assertEqual(str(next(matrix_iter)), '1')
        self.assertEqual(str(next(matrix_iter)), '-1')
        self.assertEqual(str(next(matrix_iter)), '4')
        with self.assertRaises(StopIteration):
            next(matrix_iter)



if __name__ == '__main__':
    unittest.main()