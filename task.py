list1=[]
rangevalue=int(input("enter the range"))
for i in range(rangevalue):
  value=int(input("enter the value"))
  list1.append(value)
print(list1)
a=list1[0]
b=list1[0]
for i in list1:
  if i > a:
       a=i
  elif i<b:
       b=i
print(a, " is the largest number")
print(b," is the smallest number")
