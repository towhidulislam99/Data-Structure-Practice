
# l3 = []
# how_many = int(input("How many value to inputin this List: "))

# for i in range(how_many):
    
#     new = input("Enter The Value....")
#     l3.append(new)
    
#     print(l3)
    
    
list = [1, 4, 5, 2, 3, 6, 7, [0, 9], 6, 5, [2, 5] ]
list1 = ["bangla", "english"]
    
print(list)

list2 = [2, 4, 5, 7]

list.extend(list2)
print(list)

list.append(11)
print(list)

print(list[-1])

list.insert(0, "FAQ")
print(list)

list1.count({1, 2, 3, 4})

print(list1)
list.remove('FAQ')
print(list)
list10 = [1, 3, 5, 10]
list10.sort()
print(list10)
list10.reverse()
print(list10)