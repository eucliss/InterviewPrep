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
#
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
# lst = [1,2,3,1,2,1,1,1,5,6,3,3,3,1]
# # lst = [1,2,3,3]
#
# def majorityItem(lst):
#     max = 0
#     maj = -1
#     dct = {}
#
#     result = (0, -1)
#
#     for i in lst:
#         if i in dct:
#             continue
#         else:
#             dct[i] = lst.count(i)
#     for key, value in dct.items():
#         if value > max:
#             max = value
#             maj = key
#         elif value == max:
#             maj = -1
#     return maj
#
# print(majorityItem(lst))
#----------------------------------------------------
# string = "Hello sir this is cool Hello this sir"
#
# def shortestDistance(string):
#     string = string.split(' ')
#     dct = {}
#     for i in range(0, len(string):
#         if string[i] not in dct:
#             # index1, index2, dist
#             dct[string[i]] = (i, 0, 0)
#         else:
#             if dct[string[i[1]]] == 0:
#                 dct[string[i]] = [dct[string[i[0], i, abs(dct[string[i[0] - i)]]]]]
#             else:
#                 curr = i - dct[string[i[1]]]
#                 if curr < dct[string[i[2]]]:
#                     dct[string[i]] = (dct[string[i][]])
#----------------------------------------------------
# class Solution:
#     # @param A : integer
#     # @return a list of integers
#     def primesum(self, A):
#         results = []
#         primes = self.generatePrimes(A)
#         for i in primes:
#             if A - i in primes:
#                 results.append((min(i, A-i), max(i, A-i)))
#         if len(results) != 0:
#             smaller = self.lexico(results)
#             return str(smaller[0][0]) + " + " + str(smaller[0][1]) + " = " + str(A)
#         return str(results[0][0]) + " + " + str(results[0][1]) + " = " + str(A)
#
#     def lexico(lst):
#         mins = results[0]
#         for i in range(1, len(results)):
#             if mins[0] < results[i][0] or mins[0] == results[i][0] and mins[1] < results[i][1]:
#                 continue
#             else:
#                 mins = results[i]
#         return mins
#
#
#     def generatePrimes(self, A):
#         primes = []
#         for num in range(2,A):
#             prime = True
#             for i in range(2,num):
#                 if (num%i==0):
#                     prime = False
#             if prime:
#                primes.append(num)
#         return(primes)

# class Solution:
#     def primesum(self, n):
#         for i in xrange(2, n):
#             if self.is_prime(i) and self.is_prime(n - i):
#                 return i, n - i
#
#     def is_prime(self, n):
#         if n < 2:
#             return False
#
#         for i in xrange(2, int(n**0.5) + 1):
#             if n % i == 0:
#                 return False
#
#         return True

#----------------------------------------------------
#
# INT_MAX = 4294967296
# INT_MIN = -4294967296
#
# # A binary tree node
# class Node:
#
#     # Constructor to create a new node
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None
#
#
# # Returns true if the given tree is a binary search tree
# # (efficient version)
# def isBST(node):
#     return (isBSTUtil(node, INT_MIN, INT_MAX))
#
# # Retusn true if the given tree is a BST and its values
# # >= min and <= max
# def isBSTUtil(node, mini, maxi):
#
#     # An empty tree is BST
#     if node is None:
#         return True
#
#     # False if this node violates min/max constraint
#     if node.data < mini or node.data > maxi:
#         return False
#
#     # Otherwise check the subtrees recursively
#     # tightening the min or max constraint
#     return (isBSTUtil(node.left, mini, node.data -1) and
#           isBSTUtil(node.right, node.data+1, maxi))
#
# # Driver program to test above function
# root = Node(4)
# root.left = Node(2)
# root.right = Node(5)
# root.left.left = Node(1)
# root.left.right = Node(3)
#
# if (isBST(root)):
#     print("Is BST")
# else:
#     print("Not a BST")

#----------------------------------------------------
#----------------------------------------------------
#----------------------------------------------------
#----------------------------------------------------
#----------------------------------------------------
#----------------------------------------------------
#----------------------------------------------------
#----------------------------------------------------
#----------------------------------------------------
#----------------------------------------------------
