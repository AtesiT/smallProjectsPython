import random

def roll_dice():
    roll = input('Бросить кости? Да/Нет: ')
    while roll.lower() == 'Да'.lower():
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        print('Кости выпали: {} and {}'.format(dice1, dice2))
        roll = input('Бросить кости снова? Да/Нет: ')

roll_dice()
