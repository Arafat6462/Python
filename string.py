# three way of string

'Hi there 23'  # string
"Hi there"  # string
long_string = ''' Wow 0 0 ---
hi
2 2
34 4
hello '''  # multi line string

print(type("hello there 24!"))
print(type('hello there 24!'))
print(long_string)

username = 'supercoder'
password = 'supersecret'

first_name = 'arafat'
last_name = 'nipu'
full_name = first_name + ' ' + last_name
print("full name is : " + full_name)

# string concatenation
print('Hello' + 'Arafat')
print('Hello' + str(5))

# type conversion
print(str(100))
print(type(str(100)))
print(type(int(str(100))))
print(type(float(int(str(100)))))

# Escape sequence
weather = 'It\'s sunny'
weather = "It's sunny"
weather = "It's \"kind of\" sunny"
weather = "It's \"kind of\" \t sunny\\ \n Have a nice day."  # \t for tab
print('Escape sequence : ' + weather)

# formatted strings
print("\nFormated string")
name = 'Arafat'
age = 24
print('Hi ' + name + '. You are ' + str(age) + ' years old.')
print(f'Hi {name}. You are {age} years old.')  # f for formatted.
print('Hi {}. You are {} years old.'.format('Arafat', '25'))
print('Hi {}. You are {} years old.'.format(name, age))
print('Hi {1}. You are {0} years old.'.format(name, age))
