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
# #
# # if (isBST(root)):
# #     print("Is BST")
# # else:
# #     print("Not a BST")
#
#
# # Tree Traversals
# def inOrder(root):
#     if root != None:
#         inOrder(root.left)
#         print(root.data)
#         inOrder(root.right)
#     return
#
# def preOrder(root):
#     if root != None:
#         print(root.data)
#         preOrder(root.left)
#         preOrder(root.right)
#     return
#
# def postOrder(root):
#     if root != None:
#         postOrder(root.left)
#         postOrder(root.right)
#         print(root.data)
#     return
#
# inOrder(root)
# print("______")
# preOrder(root)
# print("______")
# postOrder(root)
# print("______")

# #----------------------------------------------------
#
# # Tree node structure
# class Node:
#
#     # Contructor to create a new node
#     def __init__(self, key):
#         self.data = key
#         self.left = None
#         self.right = None
#
#
# # This function counts the number of nodes in a binary tree
# def countNodes(root):
#     if root is None:
#         return 0
#     return (1 + countNodes(root.left) + countNodes(root.right))
#
# # This function checks if binary tree is complete or not
# def isComplete(root, index, number_nodes):
#
#     # An empty is complete
#     if root is None:
#         return True
#
#     # If index assigned to current nodes is more than
#     # number of nodes in tree, then tree is not complete
#     print(index, number_nodes)
#     if index >= number_nodes :
#         return False
#
#     # Recur for left and right subtress
#     return (isComplete(root.left , 2*index+1 , number_nodes)
#         and isComplete(root.right, 2*index+2, number_nodes)
#           )
#
# # Driver Program
#
# root = Node(1)
# root.left = Node(2)
# root.right = Node(3)
# root.left.left = Node(4)
# root.left.right = Node(5)
# root.right.left = Node(6)
# root.right.right = Node(7)
#
# node_count = countNodes(root)
# # print(node_count)
# index = 0
#
# def insert(root, node):
#     if root is None:
#         root = node
#     if root.left:
#         insert(root.left, node)
#     elif root.right:
#         insert(root.left, node)
#     elif root.right is None:
#         root.right = node
#     else:
#         root.left = node
#
# # insert(root, Node(18))
# # preOrder(root)
#
# def binaryInsert(root, node):
#    if root is None:
#         root = node
#     else:
#         if root.data < node.data:
#             if root.right is None:
#                 root.right = node
#             else:
#                 insert(root.right, node)
#         else:
#             if root.left is None:
#                 root.left = node
#             else:
#                 insert(root.left, node)

# if isComplete(root, index, node_count):
#     print("The Binary Tree is complete")
# else:
#     print("The Binary Tree is not complete")

#----------------------------------------------------



# Python program to demonstrate delete operation
# in binary search tree

# A Binary Tree Node
# class Node:
#
#     # Constructor to create a new node
#     def __init__(self, key):
#         self.key = key
#         self.left = None
#         self.right = None
#
#
# # A utility function to do inorder traversal of BST
# def inorder(root):
#     if root is not None:
#         inorder(root.left)
#         print(root.key)
#         inorder(root.right)
#
#
# # A utility function to insert a new node with given key in BST
# def insert( node, key):
#
#     # If the tree is empty, return a new node
#     if node is None:
#         return Node(key)
#
#     # Otherwise recur down the tree
#     if key < node.key:
#         node.left = insert(node.left, key)
#     else:
#         node.right = insert(node.right, key)
#
#     # return the (unchanged) node pointer
#     return node
#
# # Given a non-empty binary search tree, return the node
# # with minum key value found in that tree. Note that the
# # entire tree does not need to be searched
# def minValueNode( node):
#     current = node
#
#     # loop down to find the leftmost leaf
#     while(current.left is not None):
#         current = current.left
#
#     return current
#
# # Given a binary search tree and a key, this function
# # delete the key and returns the new root
# def deleteNode(root, key):
#
#     # Base Case
#     if root is None:
#         return root
#
#     # If the key to be deleted is smaller than the root's
#     # key then it lies in  left subtree
#     if key < root.key:
#         root.left = deleteNode(root.left, key)
#
#     # If the kye to be delete is greater than the root's key
#     # then it lies in right subtree
#     elif(key > root.key):
#         root.right = deleteNode(root.right, key)
#
#     # If key is same as root's key, then this is the node
#     # to be deleted
#     else:
#
#         # Node with only one child or no child
#         if root.left is None :
#             temp = root.right
#             root = None
#             return temp
#
#         elif root.right is None :
#             temp = root.left
#             root = None
#             return temp
#
#         # Node with two children: Get the inorder successor
#         # (smallest in the right subtree)
#         temp = minValueNode(root.right)
#
#         # Copy the inorder successor's content to this node
#         root.key = temp.key
#
#         # Delete the inorder successor
#         root.right = deleteNode(root.right , temp.key)
#
#
#     return root
#
# # Driver program to test above functions
# """ Let us create following BST
#               50
#            /     \
#           30      70
#          /  \    /  \
#        20   40  60   80 """
#
# root = None
# root = insert(root, 50)
# root = insert(root, 30)
# root = insert(root, 20)
# root = insert(root, 40)
# root = insert(root, 70)
# root = insert(root, 60)
# root = insert(root, 80)
#
# print("Inorder traversal of the given tree")
# inorder(root)
#
# print("\nDelete 20")
# root = deleteNode(root, 20)
# print("Inorder traversal of the modified tree")
# inorder(root)
#
# print("\nDelete 30")
# root = deleteNode(root, 30)
# print("Inorder traversal of the modified tree")
# inorder(root)
#
# print("\nDelete 50")
# root = deleteNode(root, 50)
# print("Inorder traversal of the modified tree")
# inorder(root)


#----------------------------------------------------

# class StopIteration(Exception):
#     def __init__(self, *args):
#         Exception.__init__(self, *args)
#
# class iterguns():
#
#     def __init__(self, limit):
#         self.limit = limit
#         self.offset = 0
#
#     def __next__(self):
#         self.offset += random.random()
#         if (self.offset > self.limit):
#             raise StopIteration("wow")
#         return self.offset
#
#     def __iter__(self):
#         return self
#
# print("------ ITERATOR -------")
# itertest = iterguns(4)
# print(next(itertest))
# print(iter(itertest))
# print("-------------")
#
#
# def generatorTest(limit):
#     offset = 0
#     while True:
#         offset += random.random()
#         yield offset
#
# print("------ GEN 1 -------")
# gen = generatorTest(3)
# print(next(gen))
# print(next(gen))
#
# def groceryGen(lst):
#     i = 0
#     while True:
#         if i >= len(lst):
#             raise StopIteration("error")
#         yield lst[i]
#         i +=1
#
# print("------ GROCERY GEN -------")
# gen = groceryGen(['eggs', 'bacon', 'milk'])
# print(next(gen))
# print(next(gen))
#


#----------------------------------------------------
import timeit

# DECORATORS

#
#
# def print_inbetween(func):
#     def func_wrapper(func):
#         print("hello")
#         return func
#     return func_wrapper(func)
#
#
#
# @print_inbetween
# def foo():
#     print("world")
#     return True
#
# def time_function(f):
#     def wrapper(*args, **kargs):
#             begin = timeit.default_timer()
#             result = f()
#             end = timeit.default_timer()
#             print("time= " + str(end-begin))
#             return result
#
#     return wrapper
#
# @time_function
# def funcy():
#     count = 0
#     for i in range(0,1000):
#         for i in range(0,1000):
#             count+=1
#     return count
#
# test = funcy()
# print(test)
#
#
# def print_inbetween(func):
#     def wrapper():
#         print("first")
#         # end = func()
#         print("last")
#         return func()
#     return wrapper
#
# @print_inbetween
# def foo():
#     print("inbetween")
#     return 1
#
# count = 0
# for i in range(0,10):
#     count += foo()
#
# print(count)


#----------------------------------------------------
# HEAPS

import heapq

# min_heap = [i*i for i in range(0,10)]
# heapq.heapify(min_heap)
# heapq.heappop(min_heap) # 0
# heapq.heappush(min_heap, 7)
# heapq.nlargest(2, min_heap) #[81,64]
# heapq.heappushpop(min_heap, 2)
# smallest = min_heap[0] # doesnt pop


# max_heap = [i*i for i in range(0,10)]
# heapq._heapify_max(max_heap)
# heapq._heappop_max(max_heap)

#----------------------------------------------------
#map, filter, reduce
#map reduce

# lst = [i for i in range(0,15)] # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
# list(map(lambda x: x+1, lst)) #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
# list(filter(lambda x: x%2==0, lst)) # [0, 2, 4, 6, 8, 10, 12, 14]
# from functools import reduce
# reduce(lambda x, y: x+y, lst) # 105


#----------------------------------------------------

# TRIES, Prefixes


# class Solution:
#     # @param A : list of strings
#     # @return a list of strings
#     def prefix(self, A):
#         tree = [0, {}]
#         for s in A:
#             node = tree
#             node[0] += 1
#             for c in s:
#                 node = node[1].setdefault(c, [0, {}])
#                 node[0] += 1
#         l = []
#         for s in A:
#             prefix = ''
#             node = tree
#             for c in s:
#                 if node[0] <= 1:
#                     l.append(prefix)
#                     break
#                 prefix += c
#                 node = node[1][c]
#             else:
#                 l.append(s)
#         return l

# Input is a list of strings, returns prefixes



#----------------------------------------------------
#----------------------------------------------------
#----------------------------------------------------
