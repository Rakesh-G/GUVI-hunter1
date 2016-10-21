num = input("Input num and K value\n")
k = int(input())

l = []
for i in num:
  l.append(i)
  
l.sort()
num = ''.join(l)

num = num[:len(num) - k]

print(num)
