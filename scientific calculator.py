import math

print("Scientific Calculator")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Exponentiation (x^y)")
print("6. Square Root")
print("7. Logarithm (base 10)")
print("8. Trigonometric Functions (sin, cos, tan)")

choice = int(input("Enter your choice (1–8): "))

if choice in [1, 2, 3, 4, 5]:
    x = float(input("Enter first number: "))
    y = float(input("Enter second number: "))

    if choice == 1:
        print("Result:", x + y)
    elif choice == 2:
        print("Result:", x - y)
    elif choice == 3:
        print("Result:", x * y)
    elif choice == 4:
        if y != 0:
            print("Result:", x / y)
        else:
            print("Error: Cannot divide by zero.")
    elif choice == 5:
        print("Result:", math.pow(x, y))

elif choice == 6:
    x = float(input("Enter number: "))
    print("Square Root:", math.sqrt(x))

elif choice == 7:
    x = float(input("Enter number: "))
    print("Logarithm (base 10):", math.log10(x))

elif choice == 8:
    angle = float(input("Enter angle in degrees: "))
    rad = math.radians(angle)
    print("sin:", math.sin(rad))
    print("cos:", math.cos(rad))
    print("tan:", math.tan(rad))

else:
    print("Invalid choice")
