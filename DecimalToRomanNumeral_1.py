tallies = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000}

def DecimalToRomanNumeral(num):
    Romans = []
    romans = list(tallies.keys())
    decimals = list(tallies.values())

    i = 0
    while num >= decimals[i] and i < len(decimals):
        i += 1
    i -= 1
        
    while (num >= decimals[i]):
        Romans.append(romans[i])
        num -= decimals[i]
        while num < decimals[i]:
            i -= 1
            if i < 0:
                break
    return Romans

num = int(input('Enter a number:'))
print(*DecimalToRomanNumeral(num))