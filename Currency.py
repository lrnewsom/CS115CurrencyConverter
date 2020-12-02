"""
We used "soutien-info.net/gtaconvert/" for the USD to GTA$, and then did the math based off that for the rest.
We used "myleafs.com/app/roblox/currency-converter/" for the USD to Robux, and then did the math for the rest.
We used "xe.com/currencyconverter/convert/?Amount=1&From=USD&To=XAU" for all Gold Standard conversions.
Otherwise we used google's currency converter to get these exchange rates.
"""
class Currency:
    key1 = ""
    key2 = ""
    conversion = {
        'USD': {'Euro': 0.84, 'Yen': 104.65, 'Bitcoin': 0.000063, 'Peso': 20.42, 'Pound': 0.76, 'Dong': 23176.0,
                'Robux': 286, 'GTA$': 56021.38, 'XAU': 0.000532176, 'USD': 1},

        'Euro': {'Euro': 1, 'USD': 1.19, 'Yen': 124.49, 'Bitcoin': 0.000061, 'Peso': 24.07, 'Pound': 0.90,
                 'Dong': 27615.25, 'Robux': 340, 'GTA$': 66665.45, 'XAU': 0.000613827},

        'Yen': {'Yen': 1, 'USD': 0.0096, 'Euro': 0.0080, 'Bitcoin': 0.000000492297, 'Peso': 0.19, 'Pound': 0.0072,
                'Dong': 221.78, 'Robux': 3, 'GTA$': 537.81, 'XAU': 0.00000507802},

        'Bitcoin': {'Bitcoin': 1, 'USD': 19590.70, 'Euro': 16411.42, 'Yen': 2044465.86, 'Peso': 395066.06,
                    'Pound': 14687.34, 'Dong': 452940381.50, 'Robux': 5597343, 'GTA$': 1097498100.29, 'XAU': 10.99},

        'Peso': {'Peso': 1, 'USD': 0.050, 'Euro': 0.042, 'Yen': 5.17, 'Bitcoin': 0.0000025, 'Pound': 0.037,
                 'Dong': 1147.57, 'Robux': 14, 'GTA$': 2801.07, 'XAU': 0.0000278908},

        'Pound': {'Pound': 1, 'USD': 1.33, 'Euro': 1.12, 'Yen': 139.18, 'Bitcoin': 0.000068, 'Peso': 26.89,
                  'Dong': 30878, 'Robux': 380, 'GTA$': 75508.44, 'XAU': 0.000750296},

        'Dong': {'Dong': 1, 'USD': 0.000043, 'Euro': 0.000036, 'Yen': 0.0045, 'Bitcoin': 0.00000000219102,
                 'Peso': 0.00087, 'Robux': 0.00000015, 'GTA$': 2.41, 'XAU': 0.0000000242166, 'Pound': 0.000032},

        'Robux': {'Robux': 1, 'USD': 0.0034965, 'Euro': 0.00293706, 'Yen': 0.3659, 'Bitcoin': 0.00000022,
                  'Peso': 0.0713986, 'Pound': 0.00265, 'Dong': 81.03, 'GTA$': 195.878951, 'XAU': 0.00000186},

        'GTA$': {'GTA$': 1, 'USD': 0.00001785, 'Euro': 0.00001499, 'Yen': 0.001868, 'Bitcoin': 0.00000000112455,
                 'Peso': 0.0003645, 'Pound': 0.00001357, 'Dong': 0.4136916, 'Robux': 0.0051051,
                 'XAU': 0.0000000009499234},

        'XAU': {'XAU': 1, 'USD': 1779.07, 'Euro': 1489.48, 'Yen': 185429.44, 'Bitcoin': 0.0907152, 'Peso': 35842.05,
                'Pound': 1332.43, 'Dong': 41242933.71, 'Robux': 508306, 'GTA$': 99665961.16}
        }

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