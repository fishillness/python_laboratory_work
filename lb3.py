# Функция для получения пользовательского ввода в формате bool.
# В случае, если пользователь введет не y или n, функция будет просить ввести
# необходимые данные снова и снова
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

# Функция для считывания информации из файла и конвертации ее в словарь
def  GetDictionaryFromFile(filename):
    try:
        file = open(filename, "r")
        dictionary = {}
        # Считываем первую строку
        line = file.readline()
        # Считываем последующие строки до тех пор пока они не закончатся
        while line:
            # Разделяем строку по пробелу. В первой части будет название предмета, а во второй - вес и цена.
            item = line.split(" ")
            # Добавляем в словарь, где название предмета будет ключом, а значением - вес и цена.
            dictionary[item[0]] = item[1]
            line = file.readline()
        file.close()
        return dictionary
    except Exception as ex:
        print(ex)

# Функция  для вывода текущего словаря в консоль
def PrintDictionaty(dictionary):
    print("Текущий словарь")
    for key in dictionary:
        print(f"{key} - {dictionary[key]}")

# Функция  для поиска предмета в словаре
def GetItemInfo(dictionary):
    print("Введите название предмета, информацию о котором вы ходите посмотреть")
    item = input(": ")
    # Если предмет есть в словаре, то выводим информацию о нем
    if item in dictionary:
        print(f"{item} - {dictionary[item]}")
    # Если нет, то спрашиваем у пользователя хочет ли он добавить предмет
    else:
        answer = GetUserInputOfBool("Предмет не найден. Добавить данный предмет? y/n")
        # Если пользователь согласен добавить предмет, то просим его указать вес и цену
        if answer:
            print("Введите данные в формате: 100ml,150rub")
            itemInfo = input(": ")
            # Добавляем предмет в словарь и сохраняем данные в файл
            dictionary[item] = itemInfo
            SaveInFile("file.txt", dictionary)
            print(f"Предмет {item} добавлен.")

# Функция для сохранения словаря в файл
def SaveInFile(filename, dictionary):
    try:
        file = open(filename, "w")
        # Поочередно добавляем данные в файл
        for key in dictionary:
            line = f"{key} {dictionary[key]} \n"
            file.write(line)
        file.close()
    except Exception as ex:
        print(ex)


print("Задание")
print("Имеется словарь с описанием предметов, у которых есть 2 параметра: вес и цена. \nНеобходимо создать файл с несколькими предметами (на свое усмотрение). \nПри вводе названия предмета вывести на экран его атрибуты, \nесли нет такого предмета, то вывести сообщение «Добавить данный предмет?» и дописать его в файл.")
print()

# Считываем словарь из файла и выводим его в консоль
dictionary = GetDictionaryFromFile("file.txt")
PrintDictionaty(dictionary)
print()

# Просим пользовалеля ввести название предмета
GetItemInfo(dictionary)
