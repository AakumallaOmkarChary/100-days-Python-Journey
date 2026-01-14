print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill =0
if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("what is your age?"))
    if age<=12:
        print("please psy$ 5")
    elif age <= 18:
        print("please pay $7")
    elif age<=22:
        print("please pay 50")
    else:
        print("please pay $12")
else:
    print("Sorry you have to grow taller before you can ride.")
