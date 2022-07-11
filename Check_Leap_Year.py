def check_leap(yy):
    if ((yy % 400 == 0) or (yy % 100 != 0)) and (yy % 4 == 0):
        return True
    else:
        return False

yy = int(input('Enter the year: '))

if check_leap(yy):
    print(f'{yy} is a leap year.')
else:
    print(f'{yy} is a not leap year.')