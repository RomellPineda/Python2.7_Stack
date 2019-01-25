import unittest
# All we are doing here is defining the function without any logic. If we didn't do this, the tests would error rather than fail. When we run the test with this function defined we will get a fail instead of an error
def scale_list(l,y):
    for i in range(len(l)):
        l[i] *= y
    return l

class MainTest(unittest.TestCase):
    def test_scale_list(self):
        self.assertEqual(scale_list([1,2,3,4],5), [5,10,15,20])
        self.assertEqual(scale_list([-1,2,-3,4],-5), [5,-10,15,-20])
        self.assertEqual(scale_list([0],0), [0])