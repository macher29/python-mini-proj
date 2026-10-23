print("CALCULATOR\n")

operation = input("Operation: ")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter Second number: "))

if operation == "+":
    print(f"Sum: {num1 + num2}")

elif operation == "-":
    print(f"Sum: {num1 - num2}")

elif operation == "*":
    print(f"Sum: {num1 * num2}")

elif operation == "**":
    print(f"Sum: {num1 ** num2}")

elif operation == "/":
    print(f"Sum: {num1 / num2}")

else:
    print("Something went wrong")