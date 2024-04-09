'''
Write a decorator function calculate_time that calculates the time required for a function to run.
For example, you can use the function sum1 as an input function for your decorator.
Your file should be named decorator.py.
Please do not submit notebook files!!!
Your function should work with the following code.
Please note that you should not modify the given driver code and sum1!
'''

import time

def calculate_time(funct):
   #runs the function func and measures how long it takes to execute
   def time_finder(*args, **kwargs): #nonkeyword and keyword arguments
      start = time.time() #time() returns seconds passed since start
      get = funct(*args, **kwargs)
      finish = time.time()
      secs = finish - start

      print(f"It took {secs} sec.")
      return get
   return time_finder #sends this back to cal_time function

@calculate_time
def sum1(n):
   result = 0
   for i in range(1, n + 1):
      result += i
   return result
if __name__ == '__main__':
    n = 1000000
    s = sum1(1000000)
    print(f'The sum of numbers from 1 to {n} is {s}.')
