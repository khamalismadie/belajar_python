print("1) Square")
print("2) Triangle")
print()
menuselection = int(input("Enter a number:"))
if menuselection == 1:
    side = int(input("Enter the length of one side:"))
    area = side*side
    print("The area of your chosen shape is:", area)
elif menuselection == 2:
    base = int(input("Enter the length of base:"))
    height = int(input("Enter the height of the triangle:"))
    area = (base*height)/2
    print("The area of your chosen shape is", area)
else:
    print("Incorrect option selected")