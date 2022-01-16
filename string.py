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
print('Hi {new_name}. You are {age} years old.'.format(new_name='atik', age=100))

# access of string / string slicing
# [start]
# [start:end]
# [start:end:step over]
# [start:] -> starting point to end point
# [:end] -> starting point to end point
# [::step over] -> starting point to end point with step over
# [-1]  -> last value
# [::-1]  -> reverse value

selfish = '123456789'
print(selfish[0])
print(selfish[1])
print(selfish[2])
print(selfish)
print('range : '+selfish[0:4])
print('step range : '+selfish[0:8:2])
print('range with only start till end : '+selfish[3:])
print('range with only end point: '+selfish[:3])
print('start to end with step-over: '+selfish[::3])
print('end to start with step-over: '+selfish[7:1:-1])
print('last value: '+selfish[-1])
print('reverse value: '+selfish[::-1])

# immutability
# string are immutability. you can reassign string name='nipu'.
# but you can't change string like name[0]='a'
