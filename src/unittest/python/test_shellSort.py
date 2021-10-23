import unittest

from algorithms.shellSort import shellSort
 
class shellSortTest(unittest.TestCase):


                    def test_empty_list(self):
                                InputArray = []
                                expectedOutput =[]
                                res = list(shellSort(InputArray))
                                self.assertEqual(expectedOutput, res)


                    def test_unsorted_list(self):

                                InputArray = [3, 5, 2]
                                expectedOutput = [([2, 3, 5], -1, -1, 1, 1), ([2, 3, 5], 2, 1, -1, -1), ([2, 3, 5], 1, 0, -1, -1), ([2, 3, 5], -1, -1, 2, 0)]
                                res = list(shellSort(InputArray))
                                self.assertEqual(expectedOutput, res)


                    def test_sorted_list(self):
                                InputArray = [2, 7, 19]
                                expectedOutput = [([2, 7, 19], -1, -1, 1, 1), ([2, 7, 19], -1, -1, 2, 2)]
                                res = list(shellSort(InputArray))
                                self.assertEqual(expectedOutput, res)

                    def test_negative_numbers(self):

                                InputArray = [-7, -35, 19, -652]
                                expectedOutput = [([-652, -35, -7, 19], 1, 0, -1, -1), ([-652, -35, -7, 19], -1, -1, 1, 0), ([-652, -35, -7, 19], -1, -1, 2, 2), 
                                ([-652, -35, -7, 19], 3, 2, -1, -1), ([-652, -35, -7, 19], 2, 1, -1, -1),  ([-652, -35, -7, 19], 1, 0, -1, -1), ([-652, -35, -7, 19], -1, -1, 3, 0)]
                                res = list(shellSort(InputArray))
                                self.assertEqual(expectedOutput, res)
    


                    def test_duplicate_integers_in_list(self):
                                InputArray = [19, 7, 7, 19]
                                expectedOutput = [([7, 7, 19, 19], 1, 0, -1, -1), ([7, 7, 19, 19], -1, -1, 1, 0), ([7, 7, 19, 19], 2, 1, -1, -1), ([7, 7, 19, 19], -1, -1, 2, 1),
                                 ([7, 7, 19, 19], -1, -1, 3, 3)]
                                res = list(shellSort(InputArray))
                                self.assertEqual(expectedOutput, res)

                    def test_large_numbers(self):           

                                InputArray = [9684, 74582, 23698547, 568256]
                                expectedOutput = [([9684, 74582, 568256, 23698547], -1, -1, 1, 1), ([9684, 74582, 568256, 23698547], -1, -1, 2, 2),
                                ([9684, 74582, 568256, 23698547], 3, 2, -1, -1), ([9684, 74582, 568256, 23698547], -1, -1, 3, 2)]
                                res = list(shellSort(InputArray))
                                self.assertEqual(expectedOutput, res)


                    def test_float_number(self):
                                InputArray = [5.6, 63.2, 7.59, 168.23]
                                expectedOutput = [([5.6, 7.59, 63.2, 168.23], -1, -1, 1, 1),  ([5.6, 7.59, 63.2, 168.23], 2, 1, -1, -1),  ([5.6, 7.59, 63.2, 168.23], -1, -1, 2, 1),
                                 ([5.6, 7.59, 63.2, 168.23], -1, -1, 3, 3)]
                                res = list(shellSort(InputArray))
                                self.assertEqual(expectedOutput, res)      
if __name__ == '__main__':
    unittest.main()