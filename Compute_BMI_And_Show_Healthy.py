height = float(input('Enter your height in centimeters: ')) / 100
weight = float(input('Enter your weight in kg: '))

BMI = round(weight / height ** 2, 2)

print(f'Your BMI index is: {BMI}.  ', end='')

if BMI > 0:
    if BMI <= 16.0:
        print('You are severely underweight.')
    elif BMI <= 18.5:
        print('You are underweight.')
    elif BMI <= 25.0:
        print('You are healthy.')
    elif BMI <= 30.0:
        print('You are overweight.')
    else:
        print('You are severely overweight.')
else:
    'Enter valid details.'