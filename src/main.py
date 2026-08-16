from utils import square, is_even, celcius_to_fahrenheit

number = int(input("Enter a number: "))

print("Square:", square(number))

if is_even(number):
    print("The number is even.")
else:
    print("The number is odd.")

print("Fahrenheit equivalent:", celcius_to_fahrenheit(number))
