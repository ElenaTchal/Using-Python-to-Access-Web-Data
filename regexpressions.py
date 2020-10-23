import os  # in order to open and read the external text file
import re

file_name = os.path.join("C:/users/elena/PycharmProjects/UofMclass/regularexpressionstextfile.txt")
my_file = open(file_name)
my_file_contents = my_file.read()

# find and extract all the numbers
all_numbers = re.findall('[0-9]+', my_file_contents)

# convert the numbers from strings to int
all_numbers_integers = [int(i) for i in all_numbers]

# find sum of all numbers
print(sum(all_numbers_integers))
