#writing testscases

import unittest
from parse_csv import read_data, get_max_temp_difference, get_index


class ParseTest(unittest.TestCase):

    def setUp(self):
        self.data = 'weather.dat'


    def test_data(self):
        read_data(self.data)


    def test_read_value(self):
        self.assertEqual(read_data(self.data)[2][0], '3')

    def test_get_max_temp(self):

        self.assertEqual(get_max_temp_difference(read_data(self.data)), 45)

    #printing the results
    def test_print_results(self):

        print("Day " + str(get_index(read_data(self.data))+3))
        print("Maximum Spread " + str(get_max_temp_difference(read_data(self.data))))



if __name__ == '__main__':
    unittest.main()
