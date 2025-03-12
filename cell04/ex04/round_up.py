import math
number = input("Give me a number")

try:
    number1 = float(number)
    rounded_number1 = math.ceil(number1)
    print(rounded_number1)
except ValueError:
    print("Invalid input. Give me a number")