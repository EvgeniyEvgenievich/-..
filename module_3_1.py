calls = 0 # Это глобальная переменная, которая инициализируется нулем.
# Она используется для подсчета количества вызовов функции 'count_calls'.

def count_calls(call): # Объявление функции 'count_calls', которая принимает один аргумент 'call'.
    global calls # Это позволяет функции изменять значение глобальной переменной 'calls'. Без этой строки функция работала бы с локальной копией переменной.
    calls += call # Увеличивает значение 'calls' на значение аргумента 'call'. Например, если 'call' равен 1, то на 1 увеличивается общее количество вызовов.
    return calls # Возвращает текущее значение переменной 'calls'.


def string_info(string): # Объявление функции 'string_info', которая принимает строку 'string'.
    a = [len(string), string.upper(), string.lower()] # Создает список 'a', который содержит:'len(string)' — длину строки.'string.upper()' — строку в верхнем регистре.'string.lower()' — строку в нижнем регистре.
    count_calls(1) #'count_calls(1)' — вызывает функцию 'count_calls', чтобы увеличить счетчик вызовов на 1.
    return tuple(a) # Возвращает кортеж, созданный из списка 'a'.


def is_contains(string, list_to_search): # Объявление функции 'is_contains', которая принимает строку 'string' и список 'list_to_search'.
    b = [] # Создает пустой список 'b', который будет использоваться для хранения элементов 'list_to_search' в нижнем регистре.
    count_calls(1) #'count_calls(1)' — вызывает функцию 'count_calls', чтобы увеличить счетчик вызовов на 1.
    for i in list_to_search: # Начинает цикл по каждому элементу 'i' в 'list_to_search'.
        b.append(i.lower()) # Добавляет элемент 'i', приведенный к нижнему регистру, в список 'b'.
    return string.lower() in b # Возвращает 'True', если строка в нижнем регистре содержится в списке 'b', и 'False' в противном случае.


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)