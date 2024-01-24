#Volume/Surface Area Calculation
def volume():

  L = int(input("What is the length of your cuboid?\n"))
  W = int(input("What is the width of your cuboid?\n"))
  H = int(input("What is the height of your cuboid?\n"))
#Asking for the dimensions of the cuboid.

  V = L * W * H
#Multiplying the dimensions of the cuboid together.
  SA = (2 * (L * W)) + (2 * (L * H)) + (2 * (H * W))

  print("\n\nThe volume of your cuboid is",V,"units cubed.\n")
  print("The total surface area of your cuboid is",SA,"square units.")

#Area/Perimeter Calculation
def area():
  L = int(input("What is the length of your rectangle?\n"))
  W = int(input("What is the width of your rectangle?\n"))
#Asking for the dimensions of the rectangle.
  
  A = L * W
  P = (2 * L) + (2 * L)
#Multiplying the dimensions of the rectangle together. 
  
  print("\n\nThe area of your rectangle is",A,"square units.")
  print("\n\nThe perimeter of your rectangle is",P,"units.")

#Restaurant Tip Calculator
def tip():
  mealprice = int(input("What is the price of your meal?\n"))
  tip = int(input("What is the percentage you would like to tip?\n"))
#Asking for the meal price and the percent they want to tip.
  
  tipprice = mealprice * (tip / 100) 
  #"(tip / 100)" = just turning "tip" into a decimal to be multiplied with the price. 
  totalprice = mealprice + tipprice
#Calculating the tipped amount and the total price.
  
  print("\n\nYou are tipping", tipprice,"$.\n")
  print("The total cost of your meal (after the tip) is", totalprice,"$.")