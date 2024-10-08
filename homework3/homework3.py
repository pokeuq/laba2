from datetime import datetime

def calculate_age():
    birth_date_str = input("Введите дату рождения (дд/мм/гггг) или 'exit' для выхода: ")
    if birth_date_str.lower() == 'exit':
        print("Выход из программы.")
        return False  

    try:
        birth_date = datetime.strptime(birth_date_str, "%d/%m/%Y")
        current_date = datetime.today()
        age = current_date.year - birth_date.year
        
        if (current_date.month, current_date.day) < (birth_date.month, birth_date.day):
            age -= 1
            
        print(f"Вам - {age} лет")
    except ValueError:
        print('Неправильный ввод даты! Используйте формат дд/мм/гггг.')

    return True  

while True:
    
    if not calculate_age():
        break 

    print('')
