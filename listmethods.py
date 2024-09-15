# List methods in python

list=[2,3,5,4,7,8]
#append method adds the element to the end of the list 
list.append(11)
print(list)
#sort method helps to print the list in correct order
list.sort()
print(list)
#this makes the list in descending order
list.sort(reverse=True)
print(list)
#reverse method counts the element of the list from back
list.reverse()
print(list)
#insert method inserts in list we are inserting 6 in the third index
list.insert(3,6)
print(list)
#it gives result 3 as we inserted 6 in third index
print(list.index(6))




#concatinating in the list

a= ["red", "Blue", 1,5,7]
b=["Hello",6,"Hi"]

c= b+a
print(a)
print(b)
print(c)

#create duplicate list
d=c.copy()
print(d)
# in this case list fro d comes first and the emelments of a adds in d as d is extending
d.extend(a)
print(a)

print(d)
#['Hello', 6, 'Hi', 'red', 'Blue', 1, 5, 7, 'red', 'Blue', 1, 5, 7]