
import csv

#function to read the data without header, blank and unusable rows
def read_data(data):
    with open(data, 'r') as f:
        data = [line.split() for line in f]
        data.pop(0)
        data.pop(0)
        data.pop(8)
        data.pop(24)
        data.pop(28)
    return data

#calculating the maximum temperature difference between x[1] and x[2]
def get_max_temp_difference(parsed_data):
    maxTemp =[x[1] for x in parsed_data]
    minTemp = [x[2] for x in parsed_data]
    values = [int(x) - int(y) for x, y in zip(maxTemp, minTemp)]
    return max(values)

#getting the index of maximum temperature obtained above.
def get_index(parsed_data):
    maxTemp =[x[1] for x in parsed_data]
    minTemp = [x[2] for x in parsed_data]
    values = [int(x) - int(y) for x, y in zip(maxTemp, minTemp)]
    return values.index(max(values))


data = 'weather.dat'
read_data(data)
