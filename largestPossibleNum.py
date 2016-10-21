arr = input('')
arr = arr[1:len(arr)-1]
l = []

if ", " in arr:
  l = arr.split(", ")
else:
  l = arr.split(",")
  
l.sort(reverse = True)

op = ''
c = 0

for i in a:
  op = op + i
  c = c + 1
  if c == 3:
    op = op + ','
    c = 0
    
print(op)
