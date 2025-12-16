# Импорт функции выбора случайного числа
from random import randint

# Функция для получения пользовательского ввода в формате числа и его проверки.
# В случае, если пользователь введет не число, функция будет просить ввести
# необходимые данные снова и снова
def GetUserInputOfNumber(inputText):
    while True:
        print(inputText)
        result = input("= ")
        if result.isdigit() == False:
            print("Введите положительное число.")
        else:
            result = int(result)
            return result

# Аналогична с предыдущей  функцией, только в данном случае пользователю
# нужно ответить да или нет.
def GetUserInputOfBool(inputText):
    while True:
        print(inputText)
        result = input("= ")
        if result == "y" or result == "Y":
            return True
        elif result == "n" or result == "N":
            return False
        else:
            print("Введите y или n")

# Функция для  заполнения массива. Есть два формата заполнения:
# Ввод с консоли и заполнение случайными числами
def FillArray(n, m, random):
    array = []
    for i in range(0, n):
        row = []
        for j in range(0, m):
            if (random):
                row.append(randint(0, 100))
            else:
                text = f"[{i}][{j}] = "
                row.append(GetUserInputOfNumber(text))
        array.append(row)
    return  array

# Функция для вывода массива в консоль
def PrintArray(array):
    print()
    print("Массив: ")
    for i in range(0, n):
        for j in range(0, m):
            print(array[i][j], end=" ")
        print()

# Функция для проверки выполнения условия  задачи.
def CheckСondition(b,  n, m,  array):
    condition = False
    # Так как необходимо проверить именно столбцы, первый for начинается с j
    for j in range(0, m):
        for i in range(0, n):
            # Проверяем входит ли число в нужный промежуток и, если нет,
            # то переходим сразу к следующему столбцу, так как данный
            # столбец уже не подходит под условие задачи
            if array[i][j] < 0  or  array[i][j] > b:
                condition = False
                break
            else:
                condition = True
        # Если во всем столбце все элементы в нужном промежутке, то возвращаем
        # True и выходим из функции, так как необходимобыло найти хотя бы один столбец
        if condition:
            return True
    return  False

print("Задание")
print("Дан двумерный массив целых чисел. \nОпределить: есть ли в нем столбец, состоящий только из элементов, принадлежащих промежутку от 0 до b.")
print()

# Получаем пользовательский ввод
b =  GetUserInputOfNumber("Введите b")
n = GetUserInputOfNumber("Введите кол-во строк в массиве")
m = GetUserInputOfNumber("Введите кол-во стобцов в массиве")
getRandomNumber = GetserInputOfBool("Ввести данные массива случайным образом? y/n")
array = FillArray(n, m, getRandomNumber)
PrintArray(array)

# Вызываем функцию проверки условия и выводим ответ
print()
condition = CheckСondition(b, n, m, array)
if condition:
    print("В массиве есть нужный столбец")
else:
    print("В массиве нет нужного столбца")


