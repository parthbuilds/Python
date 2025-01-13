#list 

list = ["apple", "banana", "mango"]

print (list)
print(len(list))

# print(list[1])
print(list[-1])


thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")
  
list[1] = "mugu"
print(list)

list.append("orange")
print(list)

# list comprehension

fruits = ["apple", "banana", "cherry", "date", "elderberry"]

newlist = []
for x in fruits :
    if "a" in x:
        newlist.append(x)
        
print(newlist)


a = fruits.index("banana")
print(a)
