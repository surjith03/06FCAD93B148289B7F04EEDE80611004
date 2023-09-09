>>> def isleapYear(year):
...     if (year % 4==0 and year % 100 != 0) or year % 400 == 0:
...         return True
...     else:
...         return False
... year = int(input)
SyntaxError: invalid syntax
>>> if isleap(year):
...     print('{} is a leap year.'.format(year))
... else:
