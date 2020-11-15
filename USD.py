class USD:
    conversion = {'Euro': 0.84, 'Yen': 104.65, 'Bitcoin': 0.000063, 'Peso': 20.42, 'Pound': 0.76, 'Dong': 23176.0,
                  'Robux': 286, 'GTA$': 56021.38, 'XAU': 0.000532176}
    name = "United States Dollar ($)"
    key = ""
    amount = 0

    def __init__(self, other_currency, value):
        self.key = other_currency
        self.amount = value

    def convert(self):
        return self.amount * self.conversion[self.key]

    def show_rates(self):
        for key in self.conversion.keys():
            print("{} converts to {} at a rate of {}".format(self.name, key, self.conversion[key]))