# Try fails, jumps to Except
# wherever the code fails in the try block
a_str = 'hello'
try:
  print('before fail')
  int_str = int(a_str)   # code fails here
  print('after fail')    # this line never prints
except:
  int_str = -1           # jumps to except
print('First', int_str)  # int_str = -1


# Try works, skips Except
a_str = '123'
try:
  int_str = int(a_str)   # '123' can be converted from str to int
except:                  # skips Except
  int_str = -1 
print('Second', int_str) # int_str = 123