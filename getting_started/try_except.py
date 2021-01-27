# Try works, skips Except
a_str = '123'
try:
  int_str = int(a_str)
except:
  int_str = -1
print('Second', int_str)

# Try fails, jumps to Except
# wherever the code fails in the try block
a_str = 'hello'
try:
  print('before fail')
  int_str = int(a_str)
  print('after fail')
except:
  int_str = -1
print('First', int_str)notes
