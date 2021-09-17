maths = int(input("Enter maths mark: "))
physics = int(input("Enter maths mark: "))
chem = int(input("Enter maths mark: "))
if chem >= 50 and physics >= 55 and maths >= 65:
    if maths + physics + chem >= 190 or maths + physics >= 140:
        print('you are eligible')
    else:
        print("you are not eligible")
else:
    print("You are not eligible")
