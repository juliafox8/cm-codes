def make_triangle(n):
  for i in range(0, n):
    for j in range(0, i+1):
      if j == i:
          print('* ', end='')
      elif j == 0:
          print ('* ', end= '')
      elif i == (n - 1):
          print ('* ', end= '')
      else:
          print ("  ", end='')
    print()
    
	
