import random
from operator import itemgetter, attrgetter
#----------------------------------------------------
# # Non Dups
# names = ['Bob', 'Alice', 'Bob', 'Jill']
#
#
# # print(list(set(names)))
# print(sorted(set(names), key=names.index))
#
# nonDups = []
#
# for i in names:
#     if i in nonDups:
#         continue
#     else:
#         nonDups.append(i)
#
# print(nonDups)
#----------------------------------------------------

# 17.3
#
# l1 = [1,2,3,4,5,6,7,8,9]
#
# def randomM(l1, m):
#     L2 = []
#     while len(L2) != m:
#         rand = random.randint(0,len(l1)-1)
#         L2.append(rand)
#         del l1[rand]
#     return L2
#
# def randomRecur(l1,m):
#     return recurHelper(l1, [], m)
#
# def recurHelper(l1,l2,m):
#     if len(l2) == m:
#         return l2
#     rand = random.randint(0,len(l1)-1)
#     l2.append(l1[rand])
#     del l1[rand]
#     return recurHelper(l1, l2, m)
#
# print(randomRecur(l1,4))

#----------------------------------------------------

# Shuffle a list

# lst = [1, 2, 3, 4, 5, 6, 7, 8]
#
# def shuffle2(l):
#     if len(l) == 1:
#         return l
#     item = l[-1]
#     l2 = shuffle2(l[:-1])
#     rand = random.randint(0, len(l2))
#     l2.insert(rand, item)
#     return l2
#
# print(shuffle2(lst))
# random.shuffle(lst)
# print(lst)

#----------------------------------------------------

# print('012345'[5])
#
#
# count = 0
# for i in range(0,61524):
#     for k in str(i):
#         if k == '2':
#             count += 1
# print(count)

#----------------------------------------------------

# tallList = [(1,1), (10,10), (8,8), (9,7), (2,2), (4,4)]
#
# s = sorted(tallList, key=itemgetter(0))     # sort on secondary key
# print(sorted(s, key=itemgetter(1)))

#----------------------------------------------------
#
# x = 3
# value = 'a'
#
# result = {
#   'a': lambda x: x * 5,
#   'b': lambda x: x + 7,
#   'c': lambda x: x - 2
# }[value](x)
#
# test = lambda y: y if y > 2 else False
#
# print(test(2))
#
# print(result)
#----------------------------------------------------
#
# dict = {'a':1, 'b': 2, 'c': 3}
#
# for key, value in dict.items():
#     print(key, value)

# dict = {'a':1, 'b': 2, 'c': 3}
#
# for key in dict.keys():
#     print(key)

#----------------------------------------------------

# Input = [1 0 1 0]
# class Solution:
#     # @param A : list of integers
#     # @return an integer
#     def bulbs(self, A):
#         zero = True
#         count = 0
#         for i in range(0, len(A)):
#             if zero and A[i] == 0:
#                 A[i] = A[i] ^ 1
#                 count += 1
#                 zero = not zero
#             elif not zero and A[i] == 1:
#                 A[i] = A[i] ^ 1
#                 count += 1
#                 zero = not zero
#             else:
#                 continue
#         return count


#----------------------------------------------------
# def gcd(self, A, B):
#     if A == 0 or B == 0:
#         return A + B
#     if A == B:
#         return A
#     return self.gcd(A % B, B % A)


#----------------------------------------------------

# All Permutations

# s = "abc"
# from itertools import permutations
# s = permutations(s)
# print(s)
#
# s = "abc"
#
# def allPerms(s):
#     init = ['']
#     for i in range(0, len(s)):
#         copy = init.copy()
#         for j in range(0, len(copy)):
#             copy[j] += s[i]
#         init += copy
#     return init
#
# print(allPerms(s))
#
# def recurPerms(s):
#     return helper(s, [''])
#
# def helper(s, lst):
#     if len(s) == 0:
#         return ['']
#     lst = helper(s[:-1], lst)
#     copy = lst.copy()
#     for j in range(0, len(copy)):
#         copy[j] += s[-1]
#     return lst + copy
#
# s = 'abc'
# print(recurPerms(s))



#----------------------------------------------------
#----------------------------------------------------
#----------------------------------------------------
