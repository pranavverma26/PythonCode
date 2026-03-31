# numbers = [1,2,3,4,5,6,7,8,9,10]

# for i,j in enumerate(numbers):
#     print(i,j)

# numbers=(1,2,3,4,5,6)

# i,*j,k=numbers
# print(i)
# print(j)
# print(k)

# text = "In this tutorial we are discussing about sets"

# words = text.split()
# print(words)
# print(text)

# list1 = [1,2,2,3,3,3,4,4,4,4]

# # freq = {x:list1.count(x) for x in list1}
# # print(freq)

# # The below code is good.

# frq2 = {}
# for number in list1:
#     if number in frq2:
#         frq2[number]+=1
#     else:
#         frq2[number]=1
# print(frq2)

# words = ["1","2","3"]
# def st(word):
#     return int(word)
# print(list(map(lambda word:int(word),words)))

# students = [
#     {'name': 'Alice', 'score': 88},
#     {'name': 'Bob', 'score': 72},
#     {'name': 'Charlie', 'score': 95},
#     {'name': 'David', 'score': 65},
#     {'name': 'Eve', 'score': 78}
# ]
# sorted_students = sorted(students, key=lambda x: x['score'], reverse=True)
# print("Sorted students by score in descending order:")
# for student in sorted_students:
#     print(student)

#print(sorted(["apple", "banana", "pear"], key=len))
# ['pear', 'apple', 'banana']

# sorted(students, key=lambda x: x['score'])
# num ={1,2,3,4}
# print(num.is)

# lst1 = [1,2,3]
# lst2 = [4,5,6]
# print(lst1+lst2)
# pair = [{i:j} for i in lst1 for j in lst2]
# print(pair)
# import numpy as np
# print(np.array([1,2,3,4]))

