Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # Python 3 program to find
... # factorial of given number
... def factorial(n):
...      
...     # single line to find factorial
...     return 1 if (n==1 or n==0) else n * factorial(n - 1)
...  
... # Driver Code
... num = 5
