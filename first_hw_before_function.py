#1. The main difference between list and tuple is any updation in list allowed but not in tuple.
#2. To create empty list
#method 1
empty_list = []
#method 2
empty_list = list()

#To create empty tuple
#method 1
empty_tuple = []
#method 2
empty_tuple = tuple(())

#3. 
my_list = [1, 2, 3, 4, 5]
print(my_list[0])  #first element
print(my_list[-1])  #last element
print(my_list[1:4])  #accessing element from index 1 to 3
#here
# #4.
my_tuple = (10, 20, 30, 40, 50)
print(my_tuple[2]) #accesing third element

# my_tuple[0] = 100
# # It throws error message which is "message is 'tuple' object does not support item assignment"

#5.
# To add element to end of the list we can use append() method which will by default add element to the end.Lets take example
my_list = [1, 2, 3, 4, 5]
my_list.append(6)        # This will add element 6 to the end of my_list
print(my_list)


# use insert() method
my_list.insert(0,0)     # This  will add 0 value at 0 index
print(my_list)

# remove an element by value? 
#Use 
my_list.remove(5)        #this will remove value 5
print(my_list)

#And by index?
my_list.pop(0)          #this will remove valude of 0 index
print(my_list)

my_list.sort(reverse=False)   #Ascending order
print(my_list)               

my_list.sort(reverse=True)     #Descending order
print(my_list)      

#6.
# my_tuple.count()
# my_tuple.index()
# my_tuple.__add__()

#7.
conversion_of_list_into_tuple = tuple([1, 2, 3])
print(type(conversion_of_list_into_tuple))    #output: <class 'tuple'>

#8.
conversion_of_tuple_into_list = list([4,5,6])
print(type(conversion_of_tuple_into_list))    #output: <class 'list'>

#9.
#the purpose of len() function is to find length of any variables.
print(len(my_list))                
print(len(my_tuple))

#10.
# [1,2,3]  wrong
# [100,2,3]  right

# a = [1, 2, 3]
# b = a
# b[0] = 100
# print(a)

#11.
single_element_tuple = (2,)

#12.  the result of [1, 2] + [3, 4] would be [1,2,3,4]
    # the result of (1, 2) + (3, 4) would be (1,2,3,4)

#13.
# we can use in for existance for eg.
print(10 in my_list)   #check if value or element 10 is present in variable my_list of data type list

#14. use count() method for both tuple and list
print(my_list.count(1))
print(my_tuple.count(10))

# 15.use index() method for both tuple and list
print(my_list.index(1))
print(my_tuple.index(10))

# 16
list = [5, 2, 8, 2, 1]
first = print(list[1::])
second = print(list[0:2])
third = print(list[1::2])

#17
# using slicing
print(list[::-1])
#using reverse method
list.reverse()
print(list)

#18
# yes, tupples are immutable but we can use slicing to make a tuple reverse
print([1,2,3,4,5][::-1])

# 19
list_inside_list = [1,2,[2,3],[6]]
print(list_inside_list[0])
print(list_inside_list[1])
print(list_inside_list[2])
print(list_inside_list[3])

#20
list_inside_tuple = ([1,2],[4,5],[6,7])
# Not able to change the content in this lists because they are in a tuple and tuples are immutable.

# Real-Life Python Practice Questions
# 1
temp = float(input("Enter your temperature of your body in degree celcius:"))
if temp > 37.5:
    print("Fever Detected")

else:
    print("Normal")

# 2
givenList = ['rice','oil','salt']
for item in givenList:
    print("Added" ,item,"to your basket")

# 3
Items = ["milk", "", "bread", "", "eggs"]
for item in Items:
    if item =="":
        continue
    print(item) 

# 4
for animal in ["cat", "elephant", "dog", "tiger"]:
    if len(animal) > 5:
        print(animal)
        break
    
# 5
grades = {"Alice": 80, "Bob": 45, "Eve": 30}
for name in grades:
    if grades[name]>=40:
        print(f"{name}  sucessful people you have passed.....")
    else:
        print(f"{name} Zero bata restart yo have failed but not in life .....")


# 6
for number in range(21):
    if number%2!=0:
        print(number)
        
# 7 water level alert
initial_level = 0
while initial_level <= 100:
    print("water level:",initial_level)
    if initial_level==100:
        break
    else:
        initial_level = initial_level+10
print("Alert...ALert water level touch to 100 ")  

# 8
Names = ("Sita", "Gita", "Hari", "Nita")
name = input("What is your name:")
for naam in Names:
    if naam == name:
        print("Found.....")
        break
print("Not found....")    
    

# 9
# method1
count = 1
sentence = input("enter a sentence:")
for letter in sentence:
    if letter ==" ":
        count = count+1
print("words in sentence:",count)       

# method2
sentence1=input("Enter a sentence:")
list = sentence1.split()
print("words in sentence:",len(list))  

# 10
list2 = [3, -1, 0, 5, -7]
for num in list2:
    if num < 0:
        print(f"{num} is negative")
    elif num > 0:
        print(f"{num} is positive")
    else:
        print(f"{num} is zero")            

# 11
rooms = {"101": "yes", "102": "no", "103": "yes"}
for number,ans in rooms.items():
    if ans =="no":
        continue
    else:
        print(f"Room no:",number," is Available......")

# 12
num =3
print("For login you have only 3 attempts......")
while num>=1:
    password = input('enter password:')
    num = num-1

    if password =='admin123':
        print("password is correct")
        break
    else:
        print(f"Wrong password... \n You have {num} attempts left")
if num==0:
    print("Blocked....")

# 13
dict = {}
for i in range(3):
    item = input("Enter items:")
    price = int(input(f"Enter {item} price:"))
    dict[item] = price
print(dict)   

# 14
number_list = [2, 10, 5, 3]
max = number_list[0]
for num in number_list:
    if num >= max:
        max = num
print("maximum number in [2, 10, 5, 3] is ",max)    

# 15
total_classes_held = int(input("Enter total class held:"))
total_attended = int(input("Enter total attended class:"))
percentage = (total_attended/total_classes_held)*100
if percentage>= 75:
    print(f"your attendence is {percentage}%. So, you are eligible for exam.")
else:
    print(f"your attendence is {percentage}%. So, you are not eligible for exam.")
