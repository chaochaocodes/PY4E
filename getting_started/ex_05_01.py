'''
Week 7: Chapter 5
Write a program which repeatedly reads numbers until the user enters 'done'.
Once 'done' is entered, print out the total, count, and average of the numbers.
If the user enters anything other than a number, detect the mistake using 
try/except and print an error message, and skip to the next number.
'''
count = 0
sum = 0

while True:
  sval = input('Enter a number: ')
  if sval == 'done':
    break
  try:
    ival = int(sval)
  except:
    print('Error: Please enter a number!')
    continue

  count += 1
  sum = sum + ival

print('Numbers enter: ', count)
print('Total: ', sum)
print('Average: ', sum/count)


'''
Part 2. Print out the largest and smallest numbers entered.
'''
largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done" : break
    
    try:
        n = int(num)
    except:
        print("Invalid input")
        continue
        
    if smallest is None or largest is None:
        smallest = n
        largest = n 
    elif n < smallest:
        smallest = n
    elif n > largest:
        largest = n        

    # if smallest is None:
    #     smallest = n
    # elif n < smallest:
    #     smallest = n

    # if largest is None:
    #     largest = n
    # elif n > largest:
    #     largest = n
        
print("Maximum is", largest)
print("Minimum is", smallest)



