def hello():
  print('Hello user!')

def pack(one, two, three):
  ls = [one, two, three]
  print(ls)
  return ls

def eat_lunch(arr):
  if len(arr) == 0:
    return print('My lunchbox is empty!')
  for i in range(len(arr)):
    if i == 0:
      print(f'First I eat {arr[i]}')
    else:
      print(f'Next i eat {arr[i]}')

hello()
print('---------')
pack(1, 2, 3)
print('---------')
eat_lunch(['apple', 'sandwich', 'chips'])