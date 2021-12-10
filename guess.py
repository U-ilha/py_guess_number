chance = 3
lot = 5
difficult_1 = "1 - baby"
difficult_2 = "2 - human"
difficult_3 = "3 - machine"
difficult_4 = "4 - god among us"


def mode(difficult):
    if difficult == "1":
        print("You have choose the difficult " + difficult_1 + ". Let's Start!")
    elif difficult == "2":
        print("You have choose the difficult " + difficult_2 + ". Let's Start!")
    elif difficult == "3":
        print("You have choose the difficult " + difficult_3 + ". Let's Start!")
    elif difficult == "4":
        print("You have choose the difficult " + difficult_4 + ". Let's Start!")
    else:
        print("Sorry! Invalid option!")


def guess(chance, attempt, lot):
    if attempt != lot:
        print("Wrong, you have only more " + str(chance) + " chance")
        chance = chance - 1
        return chance
    else:
        print("YOU WIN!!!")


print("List of difficult")
print(difficult_1)
print(difficult_2)
print(difficult_3)
print(difficult_4)

difficult = input("Type the number of your difficult: ")

mode(difficult)

attempt = input("Choose a number between 1 and 10: ")

guess(chance, attempt, lot)
