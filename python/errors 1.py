
### Author : Larry Grace
## Due : 1/28/2018


 word' = SyntaxError: EOL while scanning string literal
a =NameError: name 'a' is not defined
9* (2/0)= ZeroDivisionError: division by zero
'2' + 2 = TypeError: must be str, not int

>>> suits = ["Clubs", "Diamonds", "Hearts", "Spades"] 
>>> print suits[4] 
Traceback (most recent call last): 
  File "<stdin>", line 1, in <module> 
IndexError: list index out of range



>>> int("dog") 
ValueError: int() cannot convert 'dog' into an integer.


>>> anInt = 8 
>>> anInt.append(4) # Whoops! 
Traceback (most recent call last): 
  File "<stdin>", line 1, in <module> 
AttributeError: 'int' object has no attribute 'append' 

>>> print instDictionary['Percussion'] 
Traceback (most recent call last): 
  File "<stdin>", line 1, in <module> 
KeyError: 'Percussion'

def schrödinger(): 
    if random.randrange(0,61) == 23:
       contents = "An erstwhile vivacious kitty..." 
    print contents
UnboundlocalError:
