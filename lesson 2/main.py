import random
hide_number = random.randint(1, 4)
print('***********************************')
print('** WELCOME TO GAME HIDE AND SEEK **')
print('***********************************')

user_name = input('enter your name: ')
cave = '|_|'
empty_caves = [cave] * 4
caves_not_empty = empty_caves.copy()
caves_not_empty[hide_number - 1] = '|0_0|'
empty_caves = ' '.join(empty_caves)
caves_not_empty = ' '.join(caves_not_empty)

print(f'Hello, {user_name}! where im going to hide? \n {empty_caves}')
user_answer = int(input('enter number from 1 to 4: '))
confirm = input(f'you sure entered number {user_answer}! (y/n)')

if confirm == 'n':
    print('try again')
    exit()
elif confirm == 'y':
    if user_answer == hide_number:
        print('============================')
        print(f'you win 🏆️ \nim hiding in\n{caves_not_empty}')
    else: 
        print('============================')
        print(f'you lose 😢️ \nim hiding in\n{caves_not_empty}')
else:
    print('answe y or n')
    exit()