print("PERCENTAGE CALCULATOR\n")


name = input("Name: ")
print(" ")

eng = float(input("Enter your marks in english: "))
hindi = float(input("Enter your marks in hindi: "))
maths = float(input("Enter your marks in maths: "))
sci = float(input("Enter your marks in science: "))
sst = float(input("Enter your marks in social science: "))

per = (((eng + hindi + maths + sci + sst) / 500) * 100)
percentage = round(per , 2)

print(f"{name} , Your overall percentage: {percentage}")