import random

def my_generate(count=10, start=0, stop=200):
   
    return [random.randint(start, stop) for _ in range(count)]

def find_multiples():
    
    X = input("Введите число X (от 1 до 9) или 'exit' для выхода: ")
    
    if X.lower() == 'exit':
        return False 

    try:
        X = int(X)
        if 1 <= X < 10:
            numbers = my_generate(10, 0, 200) 
            print(f"Случайные числа: {numbers}")
            multiples = list(filter(lambda num: num % X == 0, numbers))
            if multiples:
                print(f"Числа, кратные {X}: {multiples}")
            else:
                print(f"Нет чисел, кратных {X}.")
        else:
            print('Ошибка: введите число от 1 до 9.')
    except ValueError:
        print('Ошибка: неправильный ввод. Пожалуйста, введите целое число.')

    return True 

while True:
    if not find_multiples():
        break  

    print('')
