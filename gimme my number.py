userstring = input("Gimme a number that is greater than 100")
usernum = int(userstring, 10)
while (usernum < 100):
    print(usernum , " is less then 100, dummy,")
    userstring = input("Try again I've got all day")
    usernum = int(userstring, 10)

print("Good job!" , usernum , " is greater than 100")
