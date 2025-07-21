
from random import randint
import string

def id():
    y=randint(100,900)
    return str(y)
    
def last():
    j=input('lname?   ')
    return j
 
q=id().join(last())
print (q) 