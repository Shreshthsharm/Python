n=int(input("enter number ="))
list1=[]
for i in range(n):
    x=int(input("items = "))
    list1.append(x)
for  i in list1:
 if i % 2 == 0:
     print(i,'item is  even number')
else:
     print(i,"item is odd number")