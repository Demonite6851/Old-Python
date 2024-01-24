num1 = int(input("Choose your first number.\n"))
num2 = int(input("\nChoose your second number.\n"))
selection = int(input("\nChoose an operation. (1 for addition, 2 for subtraction, 3 for multiplication, and 4 for division.)\n"))
while selection < 1 or  selection > 4:
  print("Invalid input.")
  selection = int(input("Choose an operation. (1 for addition, 2 for subtraction, 3 for multiplication, and 4 for division.)\n"))
  
def add(num1,num2):
  sum = num1 + num2
  return sum
  
def subtract(num1,num2):
  difference = num1 - num2
  return difference
  
def multiply(num1,num2):
  product = num1 * num2
  return product
  
def divide(num1,num2):
  quotient = num1 / num2
  return quotient


if selection == 1:
  print("\n\n",num1,"plus",num2,"equals",add(num1,num2))
elif selection == 2:
  print("\n\n",num1,"minus",num2,"equals",subtract(num1,num2))
elif selection == 3:
  print("\n\n",num1,"times",num2,"equals",multiply(num1,num2))
elif selection == 4:
  print("\n\n",num1,"divided by",num2,"equals",divide(num1,num2))