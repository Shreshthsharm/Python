#list can store multiolke data,data can be different types int str
#list can store the  duplicate data
#list is an orsdered data set - sorting assending desending
#creat list and sttore the your friends name 
friendlist=["Ansh","kanak","vishal","prabhat","toni","nikhil","srjan"]
#print the list of friend names
print(friendlist)
#add the age of your frinds into list
#append will add the data into end of the list
friendlist.append(20)
friendlist.append(22)
friendlist.append(21)
friendlist.append(18)
friendlist.append(18)
friendlist.append(22)
friendlist.append(20)
print(friendlist)
#add  the data into list using index no
friendlist.insert(3,"SHRESHTH SHARMA")
print (friendlist)
#into access the data using index no
print(friendlist[3])
#access the complete list
# for name in friendlist:
 # print(friendlist.[2])
 # to delete the data from list
friendlist.remove("vishal")
print(friendlist)
 #pop will delet the data  using index
friendlist.pop(5)
print(friendlist)
#add fav city my
fevcity=[ "rishikes","mathura","vrindhavan", "ujjain","khatu"]
print(fevcity)
#add city ksol
fevcity.insert(0,"kasol")
print(fevcity)
# remove last city in list -using pop
fevcity.pop(5)
print(fevcity)
#sorting list
fevcity.sort()
print(fevcity)