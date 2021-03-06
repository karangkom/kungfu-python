# 1. Strings
print('This is using single quotation marks')
print("This is using double quotation marks")
print("""
This is multiline strings and using triple quote This is multiline strings and using triple quote 
""")
print("Create a single 'quote' in double quotation marks")
print('Create double "quote" in double quotation marks')
print("""
Dialogue
Mark: "Hello adam, where are you going bro?"
Adam: "I'm going to school"
Mark: "How do you go to school?"
Adam: "I go to school by bus"
""")
print() # we can create a new line using empty print()

# 2. Escape Characters
print('You can create \na new line...')
print('Quote (\') in single quotation marks')
print("Adam: \"Hello, this is my quote\"")
print(r'C:\network') # this is raw string, it create \n to a normal string

# 3. Assign String to a Variable
a = '\nHello World'
print(a)

# 4. String Concatenation
text1 = 'My'
text2 = 'Name'

print(text1 + text2) # without space
print(text1 , text2) # there is a space in the text
print('%s %s' % (text1, text2)) # formatted string 1
print(f'{text1} {text2}') # formatted string 2