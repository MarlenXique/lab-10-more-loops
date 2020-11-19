maximum_stories = 6
userstring = input("On what floor of your building is your office")
usernum = int(userstring, 10)
while (usernum > maximum_stories):
    print("You Entered: ", usernum, " but there are only ", maximum_stories, " floors in this building.")
    userstring = input("Try again")
    usernum = int(userstring, 10)
print("Congrats! You work on floor: ", usernum)
