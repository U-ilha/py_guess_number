import random

chance = 3
num = 0
difficult_1 = "1 - baby (1 to 3)"
difficult_2 = "2 - human (1 to 10)"
difficult_3 = "3 - machine (1 to 25)"
difficult_4 = "4 - god among us (1 to 100)"


def mode(difficult, num):
    if difficult == 1:
        print("You have choose the difficult {}. Let's start!".format(difficult_1))
        num = random.randrange(1, 3)
        return num
    elif difficult == 2:
        print("You have choose the difficult {}. Let's start!".format(difficult_2))
        num = random.randrange(1, 10)
        return num
    elif difficult == 3:
        print("You have choose the difficult {}. Let's start!".format(difficult_3))
        num = random.randrange(1, 25)
        return num
    elif difficult == 4:
        print("You have choose the difficult {}. Let's start!".format(difficult_4))
        num = random.randrange(1, 100)
        return num
    else:
        print("Sorry! Invalid option!")


def guess(chance, attempt, num):
    if attempt == num:
        print("YOU WIN!!!")
    else:
        print("Wrong, you have only more {} chance".format(chance))
        chance = chance - 1
        return chance


print("List of difficult")
print(difficult_1)
print(difficult_2)
print(difficult_3)
print(difficult_4)

difficult = int(input("Type the number of your difficult: "))

num = mode(difficult, num)

print(num)

attempt = int(input("Choose a number: "))

guess(chance, attempt, num)
