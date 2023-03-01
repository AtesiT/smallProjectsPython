import string
import random

characters = list(string.ascii_letters + string.digits + '!@#$%^&*()')
print(characters)
ask = input('Вы хотите сгенерировать пароль? Да/Нет: ' ) 
if ask.lower == 'Да':
    length_password = input('Введите длину пароля: ')
elif ask.loser == 'Нет':
    ervwe
else:
    print('Вы ошиблись в написании')