import unittest

from algorithms.radixSort import radixSort

class radixSortTest(unittest.TestCase):

    def test_empty_list(self):
        inputArray = [0]
        expectedOutputArray = []
        OutputArray = list(radixSort(inputArray, 0, len(inputArray)-1))
        self.assertEqual(expectedOutputArray, OutputArray)


    def test_sorted_list(self):
        inputArray = [3, 8, 34, 56, 105]
        expectedOutputArray = [3, 8, 34, 56, 105]
        OutputArray = list(radixSort(inputArray, 0, len(inputArray)-1))[0][0]
        self.assertEqual(expectedOutputArray, inputArray)

    def test_unsorted_list(self):
        inputArray = [17, 3, 8, 34, 56]
        expectedOutputArray = [3, 8, 17, 34, 56]
        OutputArray = list(radixSort(inputArray, 0, len(inputArray)-1))[0][0]
        self.assertEqual(expectedOutputArray, inputArray)


    def test_large_numbers(self):
        inputArray = [2365975885, 256987, 529, 52397]
        expectedOutputArray = [529, 52397, 256987, 2365975885]
        OutputArray = list(radixSort(inputArray, 0, len(inputArray)-1))[0][0]
        self.assertEqual(expectedOutputArray, inputArray)

    
    def test_duplicate_integers_in_list(self):
        inputArray = [7, 7, 7, 7]
        expectedOutputArray = [7, 7, 7, 7]
        list(radixSort(inputArray, 0, len(inputArray)-1)) [0][0]
        self.assertEqual(expectedOutputArray, inputArray)        


        
if __name__ == '__main__':
    unittest.main()
