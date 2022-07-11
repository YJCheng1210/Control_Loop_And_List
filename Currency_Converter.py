from forex_python.converter import CurrencyRates
c = CurrencyRates()
from_currency = input('From Currency: ').upper()
to_currency = input('To Currency: ').upper()
result = c.convert(from_currency, to_currency, 1)
if result < 1.0:
    print(to_currency, " : ", from_currency)
    print('1 : ', round(1/result, 3))
else:
    print(from_currency, " : ", to_currency)
    print('1 : ', round(result, 3))

amount = float(input(f'Enter an amount of {from_currency} you want to change to {to_currency}: '))

result *= amount
result = round(result)

print(f'{amount} {from_currency} can change to {result} {to_currency}.')