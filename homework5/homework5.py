def get_odd_numbers():
    for number in range(30):
        if number % 2 != 0:
            yield number

odd_number_generator = get_odd_numbers()

first_odd = None
fifth_odd = None
last_odd = None

for index, odd_number in enumerate(odd_number_generator, start=1):
    if index == 1:
        first_odd = odd_number
    if index == 5:
        fifth_odd = odd_number
    last_odd = odd_number

print(f"Первое нечётное число: {first_odd}")
print(f"Пятое нечётное число: {fifth_odd}")
print(f"Последнее нечётное число: {last_odd}")
