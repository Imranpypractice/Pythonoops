name = input("Enter your name:")

while name == "":
    print("You did not enter your name")
    name = input("Enter your name: no")

print(f"Hello {name}")