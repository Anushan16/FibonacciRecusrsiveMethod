
def fibGenerator(n):
  if n == 1 or n == 2:
    return 1 
  else:
    return fibGenerator(n-1)+fibGenerator(n-2)
  # test case for function
print(fibGenerator(7))

