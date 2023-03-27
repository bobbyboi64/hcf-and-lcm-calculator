first = int(input('first number'))
second = int(input('second number'))
if second > first:
  a = second
  b = first
else:
  a = first
  b = second
while True:
  if a%b == 0:
    print('hcf is '+ str(b))
    print('lcm is '+str(first*second//b))
    break
  x = a%b
  print(x)
  a = b
  b = x
