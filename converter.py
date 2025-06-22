import argparse

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def main():
    parser = argparse.ArgumentParser(description="Convert temperatures between Celsius and Fahrenheit.")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-c", "--celsius", type=float, help="Temperature in Celsius to convert to Fahrenheit.")
    group.add_argument("-f", "--fahrenheit", type=float, help="Temperature in Fahrenheit to convert to Celsius.")
    
    args = parser.parse_args()
    
    if args.celsius is not None:
        fahrenheit = celsius_to_fahrenheit(args.celsius)
        print(f"{args.celsius}°C is equal to {fahrenheit:.2f}°F")
    elif args.fahrenheit is not None:
        celsius = fahrenheit_to_celsius(args.fahrenheit)
        print(f"{args.fahrenheit}°F is equal to {celsius:.2f}°C")

if __name__ == "__main__":
    main()