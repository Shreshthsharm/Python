#error hindling
#error 1
try:
    print(x)
except:
    print("x is not defined")
    
#error2
y = "python"
z=5
try:
    c=y+z
    print(c)
except TypeError:
    print("can not string with integer")


#error3
name="shreshth"
#no =int(name)    
try:
    no=int(name)
except ValueError:
    print("string can not convert into integer")

# #error 4
friends=["shreshth","kanak","ansh"]
try:
    friends[4]
except IndexError:
    print("wrong index pass")
#error5

    


    