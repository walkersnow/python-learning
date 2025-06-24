# hari_ke_41.py
import unittest

def tambah(a, b):
    return a + b

class TestMath(unittest.TestCase):
    def test_tambah(self):
        self.assertEqual(tambah(2, 3), 5)

if __name__ == "__main__":
    unittest.main()
