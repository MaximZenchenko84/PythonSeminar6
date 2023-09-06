# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)

n = int(input('Введите количество элементов массива n = '))

arrayInput = []
for i in range(0,n):
    currentElement = int(input(f'Введите {i}-й элемент массива '))
    arrayInput.append(currentElement)

min = int(input('Введите левое значение заданного диапазона min = '))
max = int(input('Введите правое значение заданного диапазона max = '))

arrayOfIndex = []
for i in range(0,n):
    if ((arrayInput[i] >= min) and (arrayInput[i] <= max)):
        arrayOfIndex.append(i)

print(f'Массив индексов исходного массива, значения которых лежат внутри заданного диапазона')
print(arrayOfIndex)