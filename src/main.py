from utils import square, is_even, celsius_to_fahrenheit, greet

def main():
    name = input("Enter your name: ")
    print(greet(name))

    try:
        value = float(input("Enter a number: "))
    except ValueError:
        print("Invalid input. Please enter a numeric value.")
        return

    sq = square(value)
    even_odd = "even" if is_even(value) else "odd"
    fahrenheit = celsius_to_fahrenheit(value)

    print(f"Square: {sq}")
    print(f"Number is: {even_odd}")
    print(f"Fahrenheit (treating input as Celsius): {fahrenheit}")

if __name__ == "__main__":
    main()
