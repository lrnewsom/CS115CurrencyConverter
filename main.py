from Currency import Currency
from GUI import GUI


def main():
    # file_input("Pepe.txt")
    gui = input("Do you want to use the G)UI or C)onsole?: ")
    if gui == 'C':
        mode = input("Do you wish to import custom currencies via a file? (y or n): ")
        valid = False
        while not valid:
            if mode == "y":
                valid = True
                dic, new_name = file_input()
                o = input("What is your starting currency?")
                name = input("What do you want to convert to?")
                amount = float(input("How much do you want to convert?"))
                money = Currency(o, name, amount)
                money.add_entry(new_name, dic)
                converted = money.convert()
                # money.show_rates()
                print("Converted ${:,.2f} USD to {:,.2f} {}".format(amount, converted, name))
            elif mode == "n":
                valid = True
                original = input("What is your starting currency?")
                amount = float(input("How much do you want to convert?"))
                name = input("What do you want to convert to?")
                money = Currency(original, name, amount)
                converted = money.convert()
                # money.show_rates()
                print("Converted ${:,.2f} USD to {:,.2f} {}".format(amount, converted, name))
            else:
                print("Invalid choice, try again...")
                valid = False
    else:
        GUI.run()


def file_input():
    valid = False
    while not valid:
        filename = input("What is the name of the file?: ")
        try:
            file = open(filename)
            valid = True
        except OSError:
            print("Error opening file, check file name...")
            valid = False
        else:
            new_dictionary = {}
            """for line in file:
                print(line)
                l = line.split(' ')
                print("l = {}".format(l))
                new_dictionary[l[0]] = l[1]"""
            with file as fp:
                lines = fp.read().splitlines()
            # print(lines)
            for entry in lines:
                split = entry.split(' ')  # this makes a list object
                new_dictionary[split[0]] = int(split[1])
            # print(new_dictionary)
            file.close()
            name = input("What is the name of this currency?: ")
            return new_dictionary, name


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
