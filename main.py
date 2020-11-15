# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from USD import USD


def main():

    amount = float(input("How much money do you want to convert?"))
    name = input("What do you want to convert to?")
    money = USD(name, amount)
    converted = money.convert()
    money.show_rates()
    print("Converted {} USD to {} {}".format(amount, converted, name))

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
