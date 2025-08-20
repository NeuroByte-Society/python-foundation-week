import unittest

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

class TestPrime(unittest.TestCase):
    def test_small_numbers(self):
        self.assertFalse(is_prime(1))   # 1 is not prime
        self.assertTrue(is_prime(2))    # 2 is prime
        self.assertTrue(is_prime(3))    # 3 is prime

    def test_composites(self):
        self.assertFalse(is_prime(4))   # 4 is not prime
        self.assertFalse(is_prime(9))   # 9 is not prime

if __name__ == "__main__":
    unittest.main()
