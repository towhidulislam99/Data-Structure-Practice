
# l3 = []
# how_many = int(input("How many value to inputin this List: "))

# for i in range(how_many):
    
#     new = input("Enter The Value....")
#     l3.append(new)
    
#     print(l3)
    
    
# list = [1, 4, 5, 2, 3, 6, 7, [0, 9], 6, 5, [2, 5] ]
# list1 = ["bangla", "english"]
    
# print(list)

# list2 = [2, 4, 5, 7]

# list.extend(list2)
# print(list)

# list.append(11)
# print(list)

# print(list[-1])

# list.insert(0, "FAQ")
# print(list)

# list1.count({1, 2, 3, 4})

# print(list1)
# list.remove('FAQ')
# print(list)
# list10 = [1, 3, 5, 10]
# list10.sort()
# print(list10)
# list10.reverse()
# print(list10)

#list Comprehension Example Practice

list3 = [];
for x in range(10):
    list3.append(x);
print(list3)

list2 = [x for x in range(10)]
print(list2)

list4 = [];
for i in range(10):
    if(i % 2 == 0):
        list4.append(i)
print(list4)

list5 = [x for x in range(10) if(x % 2 == 1)]
print(list5)

list6 = ['add', 'sum', 1, 2, 3, 4]

list7 = [x for x in list6]
print(list7)

list7 = [x for x in list6 if x not in ['add', 'sum']]
print(list7)