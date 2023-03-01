import string
import random

characters = list(string.ascii_letters + string.digits + '!@#$%^&*()')
# print(characters)

def generate_password():
    password_length = int(input('Введите длину пароля: '))
    random.shuffle(characters)
    password = []
    for x in range(password_length):
        password.append(random.choice(characters))
    random.shuffle(password)
    password = ''.join(password)
    print(password)
    


ask = input('Вы хотите сгенерировать пароль? Да/Нет: ' ) 

if ask.lower() == 'да':
    generate_password()
elif ask.lower() == 'нет':
    print('Хорошего дня')
    quit()
else:
    print('Вы ошиблись в написании')
    quit()