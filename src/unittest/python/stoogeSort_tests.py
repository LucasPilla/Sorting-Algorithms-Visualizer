import unittest

from algorithms.stoogeSort import stoogeSort

 
class stoogeSortTest(unittest.TestCase):

    
    def test_empty_list(self):
     def stoogeSort(arr, l, h): 
        inputArray = []
        expectedOutputArray = []
        OutputArray = list(stoogeSort(inputArray, l, h))[0][0]
        self.assertEqual(expectedOutputArray, OutputArray)

    def test_items_unsorted(self):
     def stoogeSort(arr, l, h): 
        inputArray = [0, 3, 8, 34, 56, 105]
        expectedOutputArray = [0, 3, 8, 34, 56, 105]
        OutputArray = list(stoogeSort(inputArray, l, h))[0][0]
        self.assertEqual(expectedOutputArray, inputArray)

    
    def test_sorted_list(self):
     def stoogeSort(arr, l, h):     
        inputArray = [0, 3, 8, 34, 56, 105]
        expectedOutputArray = [0, 3, 8, 34, 56, 105]
        OutputArray = list(stoogeSort(inputArray, l, h))[0][0]
        self.assertEqual(expectedOutputArray, inputArray)


    def test_negative_numbers(self):
     def stoogeSort(arr, l, h):     
        inputArray = [-15, -35, -5, -27]
        expectedOutputArray = [-35, -27, -15,-5]
        OutputArray = list(stoogeSort(inputArray, l, h))[0][0]
        self.assertEqual(expectedOutputArray, OutputArray)

    
    def test_float_number(self):
     def stoogeSort(arr, l, h):     
        inputArray = [4.2, 9.4, 12.5]
        expectedOutputArray = [4.2, 9.4, 12.5]
        OutputArray = list(stoogeSort(inputArray, l, h))[0][0]
        self.assertEqual(expectedOutputArray, OutputArray)

    
    def test_duplicate_integers_in_list(self):
     def stoogeSort(arr, l, h):     
        inputArray = [5, 5, 5, 5]
        expectedOutputArray = [5, 5, 5, 5]
        OutputArray = list(stoogeSort(inputArray, l, h))[0][0]
        self.assertEqual(expectedOutputArray, inputArray)        


    def test_larger_integers(self):
     def stoogeSort(arr, l, h):     
        inputArray = [546, 92659872, 45, 26587]
        expectedOutputArray = [45, 546, 26587, 92659872]
        OutputArray = list(stoogeSort(inputArray, l, h))[0][0]
        self.assertEqual(expectedOutputArray, OutputArray)



if __name__ == '__main__':
    unittest.main()
