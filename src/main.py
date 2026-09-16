cat > src/main.py << 'EOF'
from utils import square, is_even, celsius_to_fahrenheit

def main():
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
EOF
