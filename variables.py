#Variables are containers for storing data values.
#Python has no command for declaring a variable.
#A variable is created the moment you first assign a value to it.   

x = 5
y = "John"
print(x)
print(y)

#Variables do not need to be declared with any particular type, and can even 
# change type after they have been set.
z = 4       # z is of type int
z = "Sally" # z is now of type str
print(z)

#If you want to specify the data type of a variable, this can be done with casting.
1 = str(3)    # x will be '3'
2 = int(3)    # y will be 3
3 = float(3)  # z will be 3.0 


#You can get the data type of a variable with the type() function.
a = 5
b = "John"
print(type(a))
print(type(b)) 

#String variables can be declared either by using single or double quotes:
4 = "John"
# is the same as
4 = 'John'


#Variable names are case-sensitive.
c = 4
C = "Sally"
#C will not overwrite c 