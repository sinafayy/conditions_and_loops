print("hello! This is a unit converter that converts kilometers to miles")

while True:
    print("Please enter a number of kilometers that you'r like to convert into miles. Enter only nummbert")

    km = input("Kilometers: ")
    km = float(km.replace(",", "."))
    miles = km * 0.621371

    print("{0} kilometers is {1} miles.".format(km, miles))
    choice = input("Would you like to do another conversion (y/n): ")

    if choice.lower() != "y" and choice.lower() != "yes":
        break