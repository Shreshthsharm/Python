#print('text is',text.replace('i am', 'Shreshtha sharma is'))
#text=["i","am","Data","Analyst"]
#print(' '.join(text))
#text='i am Data Analyst'
#print('text is',text.upper())
#text='i am Data Analyst'
#print('indaxe is',text.find('analyst'))
#   
num=int(input("enter number =>"))
fact=1
if num <0:
    print("nagetiv number ka factorial nhi hota")
else:
     for i in range(1,num+1):
      fact=fact*1
print("factorial is",fact)    