weapons = ["crowbar","bat","wrench","sword","flamethrower","hammer"]
zombieWeakness = "flamethrower"

print("You have encountered a zombie, you need to choose a weapon to fight with!\n")

print("Your options include:\n")
c1 = 0
while c1 != len(weapons):
  print(weapons[c1])
  c1 += 1
selection = int(input("\n\nWould you like to use a weapon from the list (type 1) or use your own weapon? (type 2)\n"))
while selection > 2 and selection < 1:
  print("Incorrect. Please type either 1 or 2.")
  selection = input("Would you like to use a weapon from the list (type 1) or add your own weapon to the list? (type 2)")
if selection == 1:
  weaponChoice = input("What weapon do you choose?\n")
  while weaponChoice not in weapons:
    print("That weapon is not on the list. Please choose a weapon that is in the list.\n")
    weaponChoice = input("What weapon do you choose?\n")
  if weaponChoice == zombieWeakness:
    print("You use the",weaponChoice,"to fight the zombie... and were successful! The zombie crumples into ashes.")
  else:
    print("You use the",weaponChoice,"to fight the zombie... but the zombie was not weak to it. You were swiftly defeated.")
if selection == 2:
  newWeapon = input("What weapon will you choose?\n")
  while newWeapon in weapons:
    print("That weapon is already on the list of weapons to choose from. Choose a weapon that is not.\n")
    newWeapon = input("What weapon will you choose?\n")
  print("You use the",newWeapon,"to fight the zombie... but the zombie was not weak to it. You were swiftly defeated.")