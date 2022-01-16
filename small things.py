print("Addition : ", 2 + 4)
print("Subtraction : ", 2 - 4)
print("Multiplication : ", 2 * 4)
print("Division :", 2 / 4)

print(type(2 + 2))  # 4
print(type(2 - 2))  # 0
print(type(2 * 2))  # 4
print(type(2 / 2))  # 1.0
print(2 / 2)

print(type(10 + 2.2))  # python auto convert it to float
print("power :", 2 ** 3)  # ** for power. 2^3 = 8
print("Round :", 5 // 2)  # 5/2=2.5 but it will 2
print("Modulo : ", 5 % 3)  # Reminder of 5/3 is 2.

# Math function
print("Round :", round(3.1))
print("Round :", round(3.9))
print("Round :", round(3.5))
print("Absolute :", abs(-45))

print("Binary value : ", bin(3))
print("Binary to decimal : ", int('0b11', 2))

# good practice
# variable name = sneak_case -> user_name.
# for constant use upper case PI
# don't touch it (__)dunder. __user_name

a, b, c, d = 1, 2, 3, 4  # assign all in one
print(a, b, c, d)

# statement vs expression
iq = 100
user_age = iq / 4  # iq/4 is expression which produce value and whole line is statement

# augmented assignment operator
some_value = 4
some_value += 3
print(some_value)
