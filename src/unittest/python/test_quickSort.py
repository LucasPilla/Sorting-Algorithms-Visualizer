import unittest

from algorithms.quickSort import quickSort


class QuickSortTest(unittest.TestCase):


    def test_empty_list(self):
        inputArray = []
        expectedOutputArray = []
        OutputArray = list(quickSort(inputArray, 0, len(inputArray)-1))
        self.assertEqual(expectedOutputArray, OutputArray)
    
    def test_sorted_list(self):
        inputArray = [0, 3, 8, 34, 56, 105]
        expectedOutputArray = [0, 3, 8, 34, 56, 105]
        OutputArray = list(quickSort(inputArray, 0, len(inputArray)-1))[0][0]
        self.assertEqual(expectedOutputArray, inputArray)

    def test_items_unsorted(self):
        inputArray = [7, 56, 28, 16, 89]
        expectedOutputArray = [7, 16, 28, 56, 89]
        OutputArray = list(quickSort(inputArray, 0, len(inputArray)-1))[0][0]
        self.assertEqual(expectedOutputArray, OutputArray)

  
    def test_negative_numbers(self):
        inputArray = [-15, -35, -5, -27]
        expectedOutputArray = [-35, -27, -15,-5]
        OutputArray = list(quickSort(inputArray, 0, len(inputArray)-1))[0][0]
        self.assertEqual(expectedOutputArray, OutputArray)

    
    def test_float_number(self):
        inputArray = [4.2, 9.4, 5.2, 12.5]
        expectedOutputArray = [4.2, 5.2, 9.4, 12.5]
        OutputArray = list(quickSort(inputArray, 0, len(inputArray)-1))[0][0]
        self.assertEqual(expectedOutputArray, OutputArray)

    
    def test_duplicate_integers_in_list(self):
        inputArray = [7, 7, 7, 7]
        expectedOutputArray = [7, 7, 7, 7]
        list(quickSort(inputArray, 0, len(inputArray)-1))
        self.assertEqual(expectedOutputArray, inputArray)        


    def test_larger_integers(self):
        inputArray = [546, 92659872, 45, 26587]
        expectedOutputArray = [45, 546, 26587, 92659872]
        OutputArray = list(quickSort(inputArray, 0, len(inputArray)-1))[0][0]
        self.assertEqual(expectedOutputArray, OutputArray)

        
if __name__ == '__main__':
    unittest.main()
