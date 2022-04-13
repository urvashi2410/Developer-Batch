import random
n = int(input("Enter size of the password: "))
choice = list('abcdefghijklmnopqrstuvwxyz')
capital = input("Do you want capital letters? (y/n)")

if capital == 'y' or capital == 'Y':
    choice.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

numbers = input("Do you want numbers? (y/n)")

if numbers == 'y' or numbers == 'Y':
    choice.extend(list('0123456789'))

symbols = input("Do you want symbols? (y/n)")

if symbols == 'y' or symbols == 'Y':
    choice.extend(list('''!@#$%^&*()_'''))

password = ""

for i in range(n):
    choose = random.choice(choice)
    password += choose

print(password)
