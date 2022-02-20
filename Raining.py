raining = input("Is it raining?")
raining = str.lower(raining)
if raining == "yes":
    windy = input("Is it windy?")
    windy = str.lower(windy)
    if windy == "yes":
        print("It is too windy for an umbrella")
    else:
        print("take an unbrella")
else:
        print("Enjoy your day")