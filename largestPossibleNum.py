arr = input('')
arr = arr[1:len(arr)-1]
l = []

if ", " in arr:
  l = arr.split(", ")
else:
  l = arr.split(",")
  
l.sort(reverse = True)

arr = ''.join(l)
op = ''
c = 0

for i in arr:
  op = op + i
  c = c + 1
  if c == 3:
    op = op + ','
    c = 0
    
if op.endswith(","):
	op = op[:len(op)-1]
	
print(op)
