## Python 3 fundamentals ##
from builtins import str #import

print(3+4j + 5+2j)  # comments used pound symbol
                    # complex numbers example
myVar = 3           # declaration needs no type, no let, no var, nothing at all
print(myVar)        # there is no concept of declaring a variable without assigning a value in Python

# 'day' + 1           # will not work, would work in JavaScript
print('day' + str(1))  # will work, uses a built in function
print('string')
print("string")
print('''string''') # these all work

# each object in Python has 3 attributes: type, value, id
x = 4
print(type(x), id(x)) #<class 'int'> 1745831616

# boolean expressions
True and True
True or False
not False
False is False

# ternary operator
booli = True
x = 3 if booli else 4

print(x) # 3

# conditionals
i = 4
if i < 3:
    print ('less than 3')
elif i < 5:
    print ('less than 5') # less than 5
else:
    print ('5 or more')

print ('Good %s, world!' % 'morning') # string formatting

# there is no switch case structure in python

############ container data types #####

# lists
myList = []
myList2 = list()
myList3 = ['a','9','b']
myList4 = list(myList3)
myList5 = "i'm a string, but i'm a list too" # single quote doesn't need to be escaped because string is in double quotes

myList.append('abc')
myList.insert(4, 'def')
print(myList)

### loops ####
for x in myList:
    print('for in', x)
    
while len(myList):  # len returns number of elements in a list
    print ('while' , myList.pop()) # pop returns the last element in a list, and removes that element from the list
    
for i in range(len(myList3)): # range returns an array of the indexes of the input array
    print ('in range', i, myList3[i])
    
for p in enumerate(myList3):            # better than using in range
    print ('enumerate', p)              # list is enumerated into 2-tuples with (index, value)
    
### accessing/slicing lists ###3

myList3[1:4] # returns the 2-4th elements of myList3 (indices 1-3)
myList3[0:-1:2] # from the 0 index to the 1st from the end, by 2s
'9' in myList3 # true
myList3.index('a') # 0

### strings ###
myStr = 'hello.world'
listFromStr = myStr.split('.') # ['hello','world'] ; same in JavaScript
strFromJoin = '/'.join(listFromStr) # 'hello/world' ; not the same as JavaScript (JS calling object is the array)

s = '       abc     '
s.strip()  # 'abc' ; trim in other languages

### Tuples ####

# tuples are like an immutable list, therefore they are faster and smaller

tu = ();
tup = tuple()
t = ('hello') # results in a string
t2 = ('hello',) # results in a 1-tuple
t3 = 'element1', 'element2'
t4 = ('element1', 'element2') # parenthesis are optional
t5 = tuple(['pass','in', 'a','list'])

# unpacking a tuple, similar to destructuring in es6
el1, el2 = t3 # el1 = 'element1', el2 = 'element2'

k = 5       # swap variables in python :)
e = 6
print(k, e)
k, e = e, k
print(k, e) 

# tuples can be accessed, sliced, and iterated over in the same way as lists

list(t3) # create a list by passing in a tuple, because a tuple is an iteritable

#### dictionaries ####

myDict = {'key1': 'value1','key2':'value2'} # just like JS; dictionaries are great
characters = dict(hero='Othello', villain='Iago', friend='Cassio') # alternative

if 'key1' in myDict:
    print(myDict['key1'])
    
for key, value in myDict.items(): # .items() returns a 2-tuple for each key,value pair
    print(key, value)

#### sets ####
mySet = set()
mySet = set(['Beta', 'Gamma', 'Alpha']) # sets cannot be accessed by index, but can use pop()
mySet2 = set(['Beta', 'Delta', 'Omega'])

mySet.union(mySet2); # great set methods for discrete math
mySet | mySet2

mySet.intersection(mySet2); # set(['Beta'])
mySet & mySet2

mySet.difference(mySet2)
mySet - mySet2

mySet.symmetric_difference(mySet2)
mySet ^ mySet2

###
# using zip(list1,list2) returns a list of tuples
# passing a list of tuples into dict(tuples) returns a dictionary created from the tuples
###

# else can be used in loops in python, and will only execute if the loop doesn't break before the end of execution
for x in range(1,6): # range does not include the last value
    if x % 5 == 0:
        print ('%d is a multiple of 5' % x)
        break
else:
    print ('No multiples of 5')
    
########### functions #########
def add_items(new_items, base_items=[]): #When defining default arguments, take special care with mutable data types.
    for item in new_items:                  #The instance of the default value is bound at the time the function is defined. 
        base_items.append(item)             #Consequently, there is a single instance of the mutable object that will be used across all calls to the function.
        return base_items                   # this is not the case in JS


add_items((1, 2, 3)) #[1, 2, 3]

add_items((1, 2, 3)) #[1, 2, 3, 1, 2, 3]

# special arguments

def fxn(a,b,c=None, *args, **kwargs):
    print('(a,b,c):', (a,b,c)) # (a,b,c): (1,2,3)
    print('args:', args)        # args: (4,5) # *args is a tuple containing all unspecified parameters, similar to rest parameters in JS
    print('kwargs:', kwargs)    # kwargs: {'e': 20, 'd': 10} # **kwargs is a dictionary containing all arguments passed in with the form 'key' = value
    
fxn(1,2,3,4,5,d=10,e=20) 

### Python is weird ###

def deepScope():  # in most languages, x would not be defined when being returned
    if True:        # Python creates a local namespace that is available anywhere within the function, works like var in JS
        if True:
            if True:
                x = 5
    return x

print(deepScope())

######### Classes #########

class Song(object): # list the parent as the parameter, use object if not inheriting from another class
    
    def __init__(self, title, artist): # this is a constructor, and have self as a parameter
        self.title = title
        self.__artist = artist
    def get_title(self): #all instance methods list self as a parameter, but nothing is passed in for self when calling these methods
        return self.title
    def get_artist(self):
        return self.__artist
    
    @classmethod # there is also a @staticmethod # As a result, the only real value in defining static methods is code organization.
    def create_songs(cls,songlist): # creates a static method, cls is the class and does not need to be passed in as an argument
        for artist, title in songlist: # destructuring or unpacking the songlist of tuples
            yield cls(title, artist) # yield returns a generator ???
                                    # cls calls the constructor fxn __init__
songs = (('Glen','Leave'),('Stevie', 'Lenny'))
    
for song in Song.create_songs(songs): # create songs is a static-ish method that returns a generator by using yield that can be iterated through
    print(song.title)
leave = Song('Leave', 'Glen Hansard')

#print(leave.__artist) # error, double underscore makes a member private
print(leave.get_artist())


### instance data, called properties in Python ###
@property
    def speed(self):
        return self.__speed

    @speed.setter       #setter uses property name.setter
    def speed(self, value):
        s = int(value)
        s = max(0, s)
        self.__speed = min(self.maxspeed, s)