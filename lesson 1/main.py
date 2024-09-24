import random
hide_number = random.randint(1, 4)
print('***********************************')
print('** WELCOME TO GAME HIDE AND SEEK **')
print('***********************************')

user_name = input('enter your name: ')
print(f'Hello, {user_name}! where im going to hide? \n |_| |_| |_| |_|')
user_answer = int(input('enter number from 1 to 4: '))
confirm = input(f'you sure entered number {user_answer}! (y/n)')

if confirm == 'n':
    print('try again')
    exit()
elif confirm == 'y':
    if user_answer == hide_number:
        print('============================')
        print(f'you win 🏆️ \nim hiding in cave number {hide_number}')
    else: 
        print('============================')
        print(f'you lose 😢️ \nim hiding in cave number  {hide_number}')
else:
    print('answe y or n')
    exit()



