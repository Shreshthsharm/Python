#list in python
#list store multiple data
mylist=["shreshth","ansh","kamak","shreshth"]
#tuple store multiple data
mytuple=("shreshth","ansh","kanak","shreshth")
 #set store multiple data
myset={"shreshth","ansh","kanak","shreshth"}
#dictionary store multiple data in key value pair
mydict={"name":"shreshth","email":"shreshthsharma2804@gmail.com","name":"shrseshth"}
#to check the dta type of all above data set
print("list:",type(mylist),"tuple:",type(mytuple))
print("set:",type(myset),"dict:",type(mydict))
#how to identify list,set,tupie,dictinoary
#list->[],tuple->(),set->{},dict->{:}
#access data from data set
print("list:",mylist[0])
print("tuple :",mytuple[0],"dict :",mydict["name"])
#list in python
#list store multiple data
mylist=["shreshth","ansh","kamak"]
#tuple store multiple data
mytuple=("shreshth","ansh","kanak")
#set store multiple data
myset={"shreshth","ansh","kanak"}
#dictionary store multiple data in key value pair
mydict={"name":"shreshth","email":"shreshthsharma2804@gmail.com"}
#to check the dta type of all above data set
print("list:",type(mylist),"tuple:",type(mytuple))
print("set:",type(myset),"dict:",type(mydict))
#how to identify list,set,tupie,dictinoary
#list->[],tuple->(),set->{},dict->{:}
#access data from data set
print("list:",mylist[0])
print("tuple :",mytuple[0],"dict :",mydict["name"])
#access complet data from data set
for data in mylist:
    print("list",data)
for item in myset:
    print("set:",item)
for value in mytuple:
    print("tuple",value)
for x in mydict.values():
    print("dict:",x)
            #to update the data in all data set
mylist[0]="shreshth"
print(mylist)
mydict["name"]="shreshth"
print(mydict)
# myset[0]="shreshth"
# print(myset)
# mytuple[0]="shreshth"
# print(mytuple)
#tuple,set is unchangeable
#list,dict is changeble
#list,tuple duplicate item
#set,dict no duplicate item
#add new value in dta set
mylist.append("kajal")
myset.add("kajal")
mydict.update({"name":"kajal"})
print("list",mylist,"tuple",mytuple,"dict",mydict,"set",myset)
#to remove the data from data set'
mydict.pop("name")
mylist.pop(0)
myset.remove("kanak")
print("list",mylist,"tuple",mytuple,"dict",mydict,"set",myset)
#convert tuple to list
convertlist=list(mytuple)
print(type(convertlist))

convertlist.append("pandit ji")
convertlist.pop(2)
print(convertlist)
mytuple=tuple(convertlist)
print(mytuple)