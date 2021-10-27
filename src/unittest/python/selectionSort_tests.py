import unittest

from algorithms.selectionSort import selectionSort
    

class selectionSort_tests(unittest.TestCase):
                    
                    def test_empty_list(self):
                                InputArray = []
                                expectedOutput =[]
                                res = list(selectionSort(InputArray))
                                self.assertEqual(expectedOutput, res)


                    def test_unsorted_list(self):
                                InputArray = [3, 5, 2]
                                expectedOutput = [([2, 3, 5], 0, -1, 0, -1), ([2, 3, 5], 1, -1, 0, -1), ([2, 3, 5], 2, -1, 0, -1), ([2, 3, 5], 1, -1, 1, -1), ([2, 3, 5], 2, -1, 1, -1)]
                                res = list(selectionSort(InputArray))
                                self.assertEqual(expectedOutput, res)



                    def test_sorted_list(self):
                                InputArray = [2, 7, 19]
                                expectedOutput = [([2, 7, 19], 0, -1, 0, -1), ([2, 7, 19], 1, -1, 0, -1), ([2, 7, 19], 2, -1, 0, -1), ([2, 7, 19], 1, -1, 1, -1), ([2, 7, 19], 2, -1, 1, -1)]
                                res = list(selectionSort(InputArray))
                                self.assertEqual(expectedOutput, res)

                    def test_negative_numbers(self):
    
                                InputArray = [19, -7]
                                expectedOutput = [([-7, 19], 0, -1, 0, -1), ([-7, 19], 1, -1, 0, -1)]
                                res = list(selectionSort(InputArray))
                                self.assertEqual(expectedOutput, res)            


                    def test_large_numbers(self):           
                                InputArray = [9684, 74582, 23698547, 568256]
                                expectedOutput = [([9684, 74582, 568256, 23698547], 0, -1, 0, -1), ([9684, 74582, 568256, 23698547], 1, -1, 0, -1),
                           ([9684, 74582, 568256, 23698547], 2, -1, 0, -1),
                           ([9684, 74582, 568256, 23698547], 3, -1, 0, -1),
                           ([9684, 74582, 568256, 23698547], 1, -1, 1, -1),
                           ([9684, 74582, 568256, 23698547], 2, -1, 1, -1),
                           ([9684, 74582, 568256, 23698547], 3, -1, 1, -1),
                           ([9684, 74582, 568256, 23698547], 2, -1, 2, -1),
                           ([9684, 74582, 568256, 23698547], 3, -1, 2, -1)]
                                res = list(selectionSort(InputArray))
                                self.assertEqual(expectedOutput, res)              


                    def test_float_number(self):
                                InputArray = [5.6, 63.2, 2.7]
                                expectedOutput = [([2.7, 5.6, 63.2], 0, -1, 0, -1), ([2.7, 5.6, 63.2], 1, -1, 0, -1), ([2.7, 5.6, 63.2], 2, -1, 0, -1),
                                 ([2.7, 5.6, 63.2], 1, -1, 1, -1), ([2.7, 5.6, 63.2], 2, -1, 1, -1)]
                                res = list(selectionSort(InputArray))
                                self.assertEqual(expectedOutput, res)                

                    def test_duplicate_integers_in_list(self):
                                InputArray = [19, 7, 7, 19]
                                expectedOutput = [([7, 7, 19, 19], 0, -1, 0, -1), ([7, 7, 19, 19], 1, -1, 0, -1), ([7, 7, 19, 19], 2, -1, 0, -1), ([7, 7, 19, 19], 3, -1, 0, -1), ([7, 7, 19, 19], 1, -1, 1, -1),
                                        ([7, 7, 19, 19], 2, -1, 1, -1),  ([7, 7, 19, 19], 3, -1, 1, -1), ([7, 7, 19, 19], 2, -1, 2, -1),  ([7, 7, 19, 19], 3, -1, 2, -1)]
                                
                                res = list(selectionSort(InputArray))
                                self.assertEqual(expectedOutput, res)                                                                              
if __name__ == '__main__':
    unittest.main()


