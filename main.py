# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    if name.lower().__contains__("n"):
        print("You are a trouble some fellow")

# Press the green button in the gutter to run the script.
name = input("What is your name? ")

print_hi(f"{name.lower()}")

Red = "Red"
Blue = "Blue"

listOfItems = []

color = input("What's your favourite color? ")

def printer():
    if len(listOfItems) == 0:
        print("list is currently empty")


if str(color) == Red.lower():
    print(f"if you chose {color} then you are wild")
# See PyCharm help at https://www.jetbrains.com/help/pycharm/


elif str(color) == Blue.lower():
    print(f"if you chose {color} then you are cool")

else:
    print("we currently don't have a match for your color")


printer()
def adder(sth):
    listOfItems.insert(0, sth)


shop = input("Name sth you'll like to shop for and separate them with space: ")

items = shop.split(" ")

adder(items)

arrange = []
blud = ""

lettersA = []

for item in items:
    arrange.append(item)
    splitItems = item.split()  # Split the item into separate strings
    for split in splitItems:
        print(split)
        if split.__contains__("a"):
            a = split.__contains__("a")
            lettersA.append(a)
            print(lettersA)
    # print("".join(item))

boolean = "true"


class Calculator:
    def addingFunc(number, sec):
        print(number + sec)
    def subtractFunc(number, sec):
        print(number - sec)


while boolean or True:
    numb = input("enter a number: ")
    secnumb = input("enter a second number: ")
    enteredNumb = int(numb)
    secenteredNumb = int(secnumb)
    sign = input("choose a sign: + or -: ")
    if str(sign).lower() == "+":
        Calculator.addingFunc(enteredNumb, secenteredNumb)
    if str(sign).lower() == "-":
        Calculator.subtractFunc(enteredNumb, secenteredNumb)

