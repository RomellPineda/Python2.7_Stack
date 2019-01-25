import unittest

def min(l):
    # Should find and return minimum value in a given list
    min = l[0]
    for val in l:
        if val < min:
            min = val
    return min
def sum_list(l):
    # Should return total value of all list items
    total = 0
    for val in l:
        total += val
    return total
def less_than(a):
    # Should return a bool of whether given value is less than 100
    return a < 100
### For this exercise, work within this class. This is something you will come up with on your own soon ###

class MainTest(unittest.TestCase):
    def test_min(self):
        self.assertEqual(min([5,4,3,2,1]), 1)
        self.assertEqual(min([-1,-2,-3,-4,-5]), -5)
        self.assertEqual(min([99,-13,'banana',42,0]), -13)

    def test_sum_list(self):
        self.assertEqual(sum_list([2,2]), 4)
        self.assertEqual(sum_list([-100,100]), 0)
        self.assertEqual(sum_list([2.5,7.5]), 10)

    def test_less_than(self):
        # returned_value = less_than(101)
        # print(returned_value)
        self.assertEqual(less_than(99), True)
        self.assertEqual(less_than(101), False)
        self.assertEqual(less_than('pineapple'), False)