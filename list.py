#=======================================
# PYTHON LIST PRACTICE
# TOPIC:LIST INDEXING AND SLICING
# ======================================
# 
# 1. Basic List Indexing

# a = ["India", "Japan", "USA", "France"]

# print(a[0][0])
# print(a[0][2])
# print(a[1][1])
# print(a[-1][-1])

# colors = ["red", "green", "blue"]

# print(colors[1][0])
# print(colors[2][2])
# print(colors[-1][0])

# v = ([30,40,35,80], [78,98,67,45], [45,32,10,90])
# print(v[0][3])
# print(v[-3][3])
# print(v[-3])
# print([0][-0])

# name = (["aakash","rahul","neha","pooja"], ["priya" ,"pooja","uditi","ayushi"], ["rekha" ,"isha","trapti","sheela"])
# print(name[-0][3])
# print(name[2][0])
# print(name[-1][3])
# print(name[1][-2])

# Mixed Data Type And Nested List

# a = [ "Hello", [1, 2, 3], "India", [True, False, [100, 200, 300]] ]

# print(a[0][1])
# print(a[1][2])
# print(a[2][3])
# print(a[3][2][1])

# x = [ "Hello", ["India", "Python"], [10, [20, 30, [40, 50]]], True ]

# print(x[1][1][0])
# print(x[2][1][2][1])
# print(x[-2][1][1])

# data = [ 100, "Python", [10, 20, 30], True, ["India", "Japan", "USA"] ]
# print(data[1])
# print(data[2][0])
# print(data[2][-1]) 
# print(data[4][1]) 
# print(data[4][-1])


# abc = [ "neha yadav",
#         18,
#         "mathura",
#        281122,
#         34536,
#         [ "false", 43, [56, [ 784547474 ]] ]
#      ]
# print( abc[5] )
# print( abc[5][2] )
# print( abc[5][2][-1] )
# print( abc[5][2][-1][-1] )

# a = 3,4,5,6,7,8,9

# print(a[:4])
# print(a[-2])

#WHITOUT LOOPS:-

# a = ["India", "Japan", "USA", "France"]

# print(a[0][0])
# print(a[0][2])
# print(a[1][1])
# print(a[-1][-1])

# colors = ["red", "green", "blue"]

# print(colors[1][0])
# print(colors[2][2])
# print(colors[-1][0])

# v = ([30,40,35,80], [78,98,67,45], [45,32,10,90])
# print(v[0][3])
# print(v[-3][3])
# print(v[-3])
# print([0][-0])

# name = (["aakash","rahul","neha","pooja"], ["priya" ,"pooja","uditi","ayushi"], ["rekha" ,"isha","trapti","sheela"])
# print(name[-0][3])
# print(name[2][0])
# print(name[-1][3])
# print(name[1][-2])

# a = [ "Hello", [1, 2, 3], "India", [True, False, [100, 200, 300]] ]

# print(a[0][1])
# print(a[1][2])
# print(a[2][3])
# print(a[3][2][1])

# x = [ "Hello", ["India", "Python"], [10, [20, 30, [40, 50]]], True ]

# print(x[1][1][0])
# print(x[2][1][2][1])
# print(x[-2][1][1])

# data = [ 100, "Python", [10, 20, 30], True, ["India", "Japan", "USA"] ]
# print(data[1])
# print(data[2][0])
# print(data[2][-1]) 
# print(data[4][1]) 
# print(data[4][-1])


# abc = [ "neha yadav",
#         18,
#         "mathura",
#        281122,
#         34536,
#         [ "false", 43, [56, [ 784547474 ]] ]
#      ]
# print( abc[5] )
# print( abc[5][2] )
# print( abc[5][2][-1] )
# print( abc[5][2][-1][-1] )

# a = 3,4,5,6,7,8,9

# print(a[:4])
# print(a[-2])

# WHITOUT LOOPS :-

# a = ["India", "Japan", "USA", "France"]

# print(a[0][0])
# print(a[0][2])
# print(a[1][1])
# print(a[-1][-1])

# colors = ["red", "green", "blue"]

# print(colors[1][0])
# print(colors[2][2])
# print(colors[-1][0])

# v = ([30,40,35,80], [78,98,67,45], [45,32,10,90])
# print(v[0][3])
# print(v[-3][3])
# print(v[-3])
# print([0][-0])

# name = (["aakash","rahul","neha","pooja"], ["priya" ,"pooja","uditi","ayushi"], ["rekha" ,"isha","trapti","sheela"])
# print(name[-0][3])
# print(name[2][0])
# print(name[-1][3])
# print(name[1][-2])

# a = [ "Hello", [1, 2, 3], "India", [True, False, [100, 200, 300]] ]

# print(a[0][1])
# print(a[1][2])
# print(a[2][3])
# print(a[3][2][1])

# x = [ "Hello", ["India", "Python"], [10, [20, 30, [40, 50]]], True ]

# print(x[1][1][0])
# print(x[2][1][2][1])
# print(x[-2][1][1])

# data = [ 100, "Python", [10, 20, 30], True, ["India", "Japan", "USA"] ]
# print(data[1])
# print(data[2][0])
# print(data[2][-1]) 
# print(data[4][1]) 
# print(data[4][-1])


# abc = [ "neha yadav",
#         18,
#         "mathura",
#        281122,
#         34536,
#         [ "false", 43, [56, [ 784547474 ]] ]
#      ]
# print( abc[5] )
# print( abc[5][2] )
# print( abc[5][2][-1] )
# print( abc[5][2][-1][-1] )

# a = 3,4,5,6,7,8,9

# print(a[:4])
# print(a[-2])

# NO LOOPS:
# How do you access and print the very last element of a list?

# a = [2,3,4,5,6,7]
# print(a[-1]) 

# b = [34,657,845,87,97,56]
# print(b[-1])

#question:-2
# How do you reverse a list without using a loop or .reverse()?

# a = ["neha","somya","kajal","diviya",]
# print(a[::-1])

# a = [ 23,45,67,89,0]
# print(a[::-1])


#question:-3
#How do you add a new element to the end of a list?

# a = ['neha','somya','priya','diviya']
# a.append ('sheela')
# print( a )

# b= [45,74,84,94,]
# b.append ('34')
# print( b )

# question:-4
# how do you add a new element to the end of a list?

# a = [45,67,89,38,845]
# print(len(a))

# b = [ 'neha','shivani','kajal','preeti','jaya','siya']
# print(len(b))

# question:-5
# How do you completely empty a list?

# a = [23,5,6,7,8]
# a.clear()
# print(a)



















































