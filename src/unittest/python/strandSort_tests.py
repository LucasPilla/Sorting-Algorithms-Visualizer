import unittest

from algorithms.strandSort import strandSort


class strandSortTest(unittest.TestCase):


    def test_empty_list(self):
        inputArray = []
        expectedOutputArray = []
        OutputArray = list(strandSort(inputArray, 0, len(inputArray)-1))
        self.assertEqual(expectedOutputArray, OutputArray)
    
    def test_sorted_list(self):
        inputArray = [1, 3, 8, 64, 236]
        expectedOutputArray = [1, 3, 8, 64, 236]
        OutputArray = list(strandSort(inputArray, 0, len(inputArray)-1))[0][0]
        self.assertEqual(expectedOutputArray, inputArray)

    def test_items_unsorted(self):
        inputArray = [16, 56, 28, 7, 89]
        expectedOutputArray = [7, 16, 28, 56, 89]
        OutputArray = list(strandSort(inputArray, 0, len(inputArray)-1))[0][0]
        self.assertEqual(expectedOutputArray, OutputArray)

  
    def test_negative_numbers(self):
        inputArray = [-15, -35, -5, -27]
        expectedOutputArray = [-35, -27, -15,-5]
        OutputArray = list(strandSort(inputArray, 0, len(inputArray)-1))[0][0]
        self.assertEqual(expectedOutputArray, OutputArray)

    
    def test_float_number(self):
        inputArray = [4.2, 9.4, 5.2, 12.5]
        expectedOutputArray = [4.2, 5.2, 9.4, 12.5]
        OutputArray = list(strandSort(inputArray, 0, len(inputArray)-1))[0][0]
        self.assertEqual(expectedOutputArray, OutputArray)

    
    def test_duplicate_integers_in_list(self):
        inputArray = [9, 9, 15, 22, 15]
        expectedOutputArray = [9, 9, 15, 15, 22]
        list(strandSort(inputArray, 0, len(inputArray)-1))
        self.assertEqual(expectedOutputArray, inputArray)        


    def test_larger_integers(self):
        inputArray = [2368, 92659872, 17, 26587]
        expectedOutputArray = [17, 2368, 26587, 92659872]
        OutputArray = list(strandSort(inputArray, 0, len(inputArray)-1))[0][0]
        self.assertEqual(expectedOutputArray, OutputArray)

        
if __name__ == '__main__':
    unittest.main()
