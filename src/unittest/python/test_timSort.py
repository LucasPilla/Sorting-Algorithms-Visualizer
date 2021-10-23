import unittest

from algorithms.timSort import timSort


class TimSortTest(unittest.TestCase):

    def test_empty_list(self):
        inputArray = [0]
        expectedOutput = [([0], 0, -1, 0, 0)]
        OutputArray = list(timSort(inputArray, 0, len(inputArray)-1))
        self.assertEqual(expectedOutput, OutputArray)


    def test_sorted_list(self):
        inputArray = [0, 3, 8, 34, 56, 105, 56398752]
        expectedOutput = [0, 3, 8, 34, 56, 105, 56398752]
        OutputArray = list(timSort(inputArray, 0, len(inputArray)-1))[0][0]
        self.assertEqual(expectedOutput, inputArray)

    def test_items_unsorted(self):
        inputArray = [7, 56, 28, 16, 89]
        expectedOutput = [7, 16, 28, 56, 89]
        OutputArray = list(timSort(inputArray, 0, len(inputArray)-1))[0][0]
        self.assertEqual(expectedOutput, OutputArray)

  
    def test_negative_numbers(self):
        inputArray = [-15, -35, -5, -27]
        expectedOutput = [-35, -27, -15,-5]
        OutputArray = list(timSort(inputArray, 0, len(inputArray)-1))[0][0]
        self.assertEqual(expectedOutput, OutputArray)

    
    def test_float_number(self):
        inputArray = [4.2, 9.4, 5.2, 12.5]
        expectedOutput = [4.2, 5.2, 9.4, 12.5]
        OutputArray = list(timSort(inputArray, 0, len(inputArray)-1))[0][0]
        self.assertEqual(expectedOutput, OutputArray)

    
    def test_duplicate_integers_in_list(self):
        inputArray = [7, 7, 7, 7]
        expectedOutput = [7, 7, 7, 7]
        list(timSort(inputArray, 0, len(inputArray)-1))
        self.assertEqual(expectedOutput, inputArray)        


    def test_large_numbers(self):
        inputArray = [538, 9532953954545, 56398752, 2654]
        expectedOutput = [538, 2654, 56398752, 9532953954545]
        OutputArray = list(timSort(inputArray, 0, len(inputArray)-1))[0][0]
        self.assertEqual(expectedOutput, inputArray)



        
if __name__ == '__main__':
    unittest.main()
