import unittest
# Notice that we are now importing unittest
def sum_two(a,b):
    return a + b
# Below this line we are creating our first class that will hold all of our tests
class MainTest(unittest.TestCase):
    # We will create individual tests as methods within this class, and the system knows to run any method whose name begins with 'test'
    def test_hello(self):
        print("Hello from the tests")

    def test_sum_two(self):
        returned_value = sum_two(5,7)
        # Here we call on self, and utilizing the methods we inherited from TestCase we can call on the assertEqual method, providing our inputs
        self.assertEqual(returned_value, 12)

        self.assertEqual(sum_two(-5,5), 0)