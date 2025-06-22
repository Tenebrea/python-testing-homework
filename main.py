def calculate_average(numbers: list[float]) -> float|None:
    if not numbers:#При пустом списке возврат None
        return None
    return round(sum(numbers) / len(numbers))#Возврат среднего значения с округлением до целого числа

def show_result(data):
    if data is not None: #Возврат при не пустом списке
        print(f'Среднее значение: {data:.2f}')
    else: #Возврат при пустом списке
        print(data)

def main():
    numbers = list(map(float, input('Пожалуйста, введите числа через пробел: ').split())) #Получение из строки списка чисел
    res = calculate_average(numbers) #Вычисление среднего значения
    show_result(res) #Вывод результата


