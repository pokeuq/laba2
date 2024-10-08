import random

def show_choice(option):
    if option == 1:
        print('Камень')
    elif option == 2:
        print('Ножницы')
    elif option == 3:
        print('Бумага')
    else:
        print('Ошибка! Неверный выбор')

def determine_winner(player_choice):
    random_choice = random.randint(1, 3) 
    show_choice(random_choice)
    
    if player_choice == random_choice:
        print('Ничья')
    elif (random_choice == 1 and player_choice == 2) or \
         (random_choice == 2 and player_choice == 3) or \
         (random_choice == 3 and player_choice == 1):
        print('Поражение')
    else:
        print('Победа')

def main():
    options = {1: 'Камень', 2: 'Ножницы', 3: 'Бумага'}

    while True:
        print('1 - Камень')
        print('2 - Ножницы')
        print('3 - Бумага')
        print('Любое другое число - выход')
        
        user_input = input("Ваш выбор (Камень, Ножницы, Бумага): ")

        try:
            choice = int(user_input)

            if choice >= 4:
                print("Выход из игры.")
                break
            else:
                print(f'Вы выбрали: {options.get(choice, "Ошибка! Неверный выбор")}')
                determine_winner(choice)
        except ValueError:
            print('Ошибка: неправильный ввод, введите число.')

        print('')
        # чтобы разделить визуально в консоли

if __name__ == "__main__":
    main()
