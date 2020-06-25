# Casting is used to convert a data type into another

# 1. Casting in user input
a = input('Input number: ') # input data type is string

print(a)
print(type(a))

b = int(input('Input number: ')) # it can change by using int() function

print(b)
print(type(b))
print()

#2. Casting using float() function
c = float(23)
print(c)
print(type(c))

#3. Casting using str() function
d = str(23)
print(d)
print(type(d))

#4. Casting using int() function
# e = int('saddam')
e = int('3')
print(e)
print(type(e)) # it can't convert to integer using alphabet, but it will works when we change the 'saddam' to the numeric

#5. Casting using tuple() function
list1 = tuple([1, 2])
print(list1)
print(type(list1))