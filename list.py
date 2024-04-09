'''
Write a function list_comprehension() that takes input as a list A
and generates a list of items B using a list comprehension in such a way
that each item in B equals to a sum of two consecutive items in the original list
A: B[i] = A[i] + A[i+1].
For example, if the original list is [1, 3, 2, 4] then the list comprehension should have
the following items: [4, 5, 6] where 4 = 1 + 3, 5 = 3 + 2, 6 = 2 + 4.
If the original list A has only one item, the comprehension list B should be empty.
NOTE: Your function should contain only two lines of code: the header and the return statement! 
'''

def list_comprehension(a):
    return [a[i]+a[i+1] for i in range(len(a)-1)]        

