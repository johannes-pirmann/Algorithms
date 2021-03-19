from bubble_sort import bubble_sort
from insertion_sort import insertion_sort
import unittest


class Testing(unittest.TestCase):
    def testinsertionsort(self):
        unordered_arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        ordered_arr = insertion_sort(unordered_arr)
        self.assertEqual(ordered_arr, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    def testbubblesort(self):
        unordered_arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        ordered_arr = bubble_sort(unordered_arr)
        self.assertEqual(ordered_arr, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
          
if __name__ == "__main__":
    unittest.main()
