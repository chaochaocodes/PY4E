'''
Finding Numbers in a Haystack

In this assignment you will read through and parse a file with text and numbers. 
You will extract all the numbers in the file and compute the sum of the numbers.

Use the Sample data to test, the sum is given for your testing.

Data Files
Sample data: http://py4e-data.dr-chuck.net/regex_sum_42.txt 
(There are 90 values with a sum=445833)

Actual data: http://py4e-data.dr-chuck.net/regex_sum_1144979.txt 
(There are 66 values and the sum ends with 796)
'''

import re

data = open('regex_sum_1144979.txt')
result = 0

for line in data:
    numbers = re.findall('[0-9]+', line)
    for number in numbers:
        result += int(number)

print(result)
# return result