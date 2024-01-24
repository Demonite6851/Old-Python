def fortune():
  name = input("What's your name?\n")
  cookienum = int(input("\nPick a number between 1 and 5.\n"))
  if(cookienum == 1):
    print("The road may seem rocky for now, "+name+", but it will smooth out eventually.")
  elif (cookienum == 2):
    print("Patience is a virtue, "+name+", and it is often rewarding.")
  elif (cookienum == 3):
    print("Don't think of rock bottom as a bad thing, "+name+". You can only go higher from here.")
  elif (cookienum == 4):
    print("Always remember, "+name+": you cannot change the future, you must always treasure the past, and don't forget to enjoy the present.")
  else:
    print("One day, "+name+", the fruits of your labor will ripen, and you will flourish knowing your hard work was worth it.")
    