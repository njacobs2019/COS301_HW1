import unittest
from vector import vector

class TestVector(unittest.TestCase):
    def test_init(self):
        v = vector()
        self.assertEqual(v.vec, [])
        
        v = vector([1, 2, 3])
        self.assertEqual(v.vec, [1, 2, 3])
        
    def test_append(self):
        v = vector()
        v.append(1)
        v.append(2)
        v.append(3)
        self.assertEqual(v.vec, [1, 2, 3])
        
    def test_add(self):
        v1 = vector([1, 2, 3])
        v2 = vector([4, 5, 6])
        v1.add(v2)
        self.assertEqual(v1.vec, [5, 7, 9])
        
    def test_add_different_lengths(self):
        v1 = vector([1, 2, 3])
        v2 = vector([4, 5])
        with self.assertRaises(SystemExit):
            v1.add(v2)
        
    def test_subtract(self):
        v1 = vector([1, 2, 3])
        v2 = vector([4, 5, 6])
        v1.subtract(v2)
        self.assertEqual(v1.vec, [-3, -3, -3])
        
    def test_subtract_different_lengths(self):
        v1 = vector([1, 2, 3])
        v2 = vector([4, 5])
        with self.assertRaises(SystemExit):
            v1.subtract(v2)
        
    def test_multiply(self):
        v1 = vector([1, 2, 3])
        v2 = vector([4, 5, 6])
        v1.multiply(v2)
        self.assertEqual(v1.vec, [4, 10, 18])
        
    def test_multiply_different_lengths(self):
        v1 = vector([1, 2, 3])
        v2 = vector([4, 5])
        with self.assertRaises(SystemExit):
            v1.multiply(v2)
        
    def test_divide(self):
        v1 = vector([4, 6, 8])
        v2 = vector([2, 3, 4])
        v1.divide(v2)
        self.assertEqual(v1.vec, [2, 2, 2])
        
    def test_divide_different_lengths(self):
        v1 = vector([1, 2, 3])
        v2 = vector([4, 5])
        with self.assertRaises(SystemExit):
            v1.divide(v2)
        
    def test_div(self):
        v1 = vector([10, 5, 7])
        v2 = vector([3, 2, 2])
        v1.div(v2)
        self.assertEqual(v1.vec, [3, 2, 3])
        
    def test_div_different_lengths(self):
        v1 = vector([1, 2, 3])
        v2 = vector([4, 5])
        with self.assertRaises(SystemExit):
            v1.div(v2)
        
    def test_negate(self):
        v = vector([1, 2, 3])
        v.negate()
        self.assertEqual(v.vec, [-1, -2, -3])
        
    def test_str(self):
        v = vector([1, 2, 3])
        self.assertEqual(str(v), "(1, 2, 3)")