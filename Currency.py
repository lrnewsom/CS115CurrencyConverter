class Currency:
    key1 = "";
    key2 = "";
    conversion = {
        'USD': {'Euro': 0.84, 'Yen': 104.65, 'Bitcoin': 0.000063, 'Peso': 20.42, 'Pound': 0.76, 'Dong': 23176.0,
                'Robux': 286, 'GTA$': 56021.38, 'XAU': 0.000532176},

        'Euro': {},

        'Yen': {},

        'Bitcoin': {},

        'Peso': {},

        'Pound': {},

        'Dong': {},

        'Robux': {},

        'GTA$': {},

        'XAU': {}
        }
    name = "United States Dollar ($)"
    amount = 0

    def __init__(self, original_currency="", other_currency="", value=0):
        self.key1 = original_currency
        self.key2 = other_currency
        self.amount = value

    def convert(self):
        return self.amount * self.conversion[self.key1][self.key2]

    """def show_rates(self):
        for key in self.conversion.keys():
            print("{} converts to {} at a rate of {}".format(self.name, key, self.conversion[key]))
    """
    def add_entry(self, name="", dic={}):
        print(dic)
        self.conversion[name] = dic
        for key in self.conversion.keys():
            for n in dic.keys():
                if key == n:
                    self.conversion[key][name] = float(1.0/dic[n])
        print(self.conversion)