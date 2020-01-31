from random import randint

answer = input('Wanna roll?')

while answer == 'yes':
    print(randint(1, 7))

    answer = input('Again?')
