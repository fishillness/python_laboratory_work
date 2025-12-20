# Импортируем библиотеки для работы с графиками и массивами
import matplotlib.pyplot as plt
import matplotlib.cbook as cbook
import numpy as np

variant = 8

# Создаем фигуру с сеткой 2х3. Задаем ей ширину и высоту
fig, ax = plt.subplots(2, 3, figsize=(16, 12))
fig.set_figwidth(9)
fig.set_figheight(7)

# Настраиваем оси для каждой клетки. У первой клетки убираем, так как там картинка
ax[0,0].axis('off')
ax[0,1].tick_params(axis='both', labelsize=12, rotation=45,  labelfontfamily='Comic Sans MS')
ax[0,2].tick_params(axis='both', labelsize=12, rotation=45,  labelfontfamily='Comic Sans MS')
ax[1,0].tick_params(axis='both', labelsize=12, rotation=45,  labelfontfamily='Comic Sans MS')
ax[1,1].tick_params(axis='both', labelsize=12, rotation=45,  labelfontfamily='Comic Sans MS')
ax[1,2].tick_params(axis='both', labelsize=12, rotation=45,  labelfontfamily='Comic Sans MS')

# =====================  [0,0] =====================

# Загружаем файл с картинкой и устанавливаем его в первую клетку. Устанавливаем заголовок в соответствии с заданием
with cbook.get_sample_data('C:\\Users\\fishi\\PycharmProjects\\python_laboratory_work\\png.jpg') as image_file:
       image = plt.imread(image_file)
ax[0,0].imshow(image)
ax[0,0].set_title("Кот", fontname='Tahoma', fontsize=14, fontweight='light', fontstyle = 'oblique', color = (0.055, 0.035, 0.286, 0.9))

# =====================  [0,1] =====================

# Построчно считываем из файла с данными и записываем строки в список
data = []
with open("data.txt") as file:
       for line in file:
              # Разделение строки на части по пробелам и преобразование каждой части во float
              data.append([float(x) for x in line.split()])

# Преобразуем первую строку и девятую в массивы NumPy
x = np.array(data[0])
y = np.array(data[variant])

# Заливаем цветом области выше и ниже нуля
ax[0,1].fill_between(x, y,  where=(y<0), color='#00bfff', alpha=0.7)
ax[0,1].fill_between(x, y, where=(y>0), color='#ffa8af', alpha=0.7)
# Устанавливаем заголовок и включаем отображение сетки
ax[0,1].set_title("График", fontname='Tahoma', fontsize=14, fontweight='light', fontstyle = 'oblique', color = (0.055, 0.035, 0.286, 0.9))
ax[0,1].grid(True)

# ===================== [0,2] =====================

# Также построчно считываем из файла с данными и записываем строки в список
data = []
with open("fig8.txt") as file:
       for line in file:
              data.append([float(x) for x in line.split()])
# Из первой строки нужного варианта берем  начальное и конечное значения интервала для оси абсцисс диаграммы
start = int(data[2*variant-2][0])
end = int(data[2*variant-2][1])
# Создаем список чисел от начального до конечного значения
x = list(range(start, end+1))
# Из второй строки нужного варианта берем оставшиеся значения
y = data[2*variant-1]

# Отрисовываем столбчатый график,устанавливаем фон, заголовок и отображение сетки
ax[0,2].bar(x, y, color = '#20b2aa')
ax[0,2].set_facecolor('#cbf2f5')
ax[0,2].set_title("Аннотация", fontname='Tahoma', fontsize=14, fontweight='light', fontstyle = 'oblique', color = (0.055, 0.035, 0.286, 0.9))
ax[0,2].grid(True)

# Вычисляем максимальное значение
maxIndex =  np.argmax(y)
selected_x = x[maxIndex]
selected_y = y[maxIndex]
# Создаем аннотацию к  максимальному значению
ax[0,2].annotate(u'Максимальный',
              xy = (selected_x, selected_y),
              xytext=(selected_x + 3, selected_y - 3),
              fontname='Arial', color = '#001d18', fontsize=13,
              fontweight='normal', fontstyle = 'normal',
              arrowprops=dict(arrowstyle="->", color= (0.055, 0.035, 0.286, 1)))

# ===================== [1,0] =====================

# Создаем массив равномерно распределенных чисел в интервале от 0 до 10
x = np.linspace(0, 10, 100)
# Записываем первую функцию
y1 = np.power((np.sin(2*x)),2)-np.power((np.cos(x)),2)

# Задаем корни многочлена
roots = [-1.9, -0.4, 0.35, 1.7]
# Получаем коэффициенты многочлена
coefficients =  np.poly(roots)
# Создаем объект многочлена
polynomial = np.poly1d(coefficients)
# Записываем вторую функцию
y2 = 0.3 * polynomial(x)

# Отрисовываем обе функции и создаем легенду к ним
ax[1,0].plot(x, y1, label='Функция y1')
ax[1,0].plot(x, y2, label='Функция y2')
ax[1,0].legend(loc='best', prop = {'family': 'Arial', 'size': 16, 'weight': 'normal', 'style': 'normal'})
# Устанавливаем заголовок,  отображение сетки и поворот подписей делений оси  ОХ
ax[1,0].set_title("Легенда", fontname='Tahoma', fontsize=14, fontweight='light', fontstyle = 'oblique', color = (0.055, 0.035, 0.286, 0.9))
ax[1,0].grid(True)
ax[1,0].tick_params(axis='both', labelsize=12, rotation=60,  labelfontfamily='Comic Sans MS')

# ===================== [1,1] =====================

# Для того, чтобы каждое распределение находилось в разных частях графика,
# мы генерируем данные по оси х в нужном диапазоне.
N = 300
points_per_dist = N // 3

# Умножаем данные на 0.33, чтобы  они были в диапазоне от 0 до 0,33
x1 = np.random.rand(points_per_dist) * 0.33
# Умножаем данные на 0.33 и добавляем 0.33, чтобы  они были в диапазоне от 0,33 до 0,66
x2 = np.random.rand(points_per_dist) * 0.33 + 0.33
# Умножаем данные на 0.33 и добавляем 0.66, чтобы  они были в диапазоне от 0,66 до 1
x3 = np.random.rand(points_per_dist) * 0.33 + 0.66

# Генерируем у координаты по закону Парето и отображаем точки
y1 = np.random.pareto (1.2,size=points_per_dist)
ax[1,1].scatter( x1, y1, color='blue', s=1)
# Генерируем у координаты по нормальному закону  распределения и отображаем точки
y2 = np.random.normal(6, 3, size=points_per_dist)
ax[1,1].scatter( x2, y2, color=(0.545, 0, 1), s=2)
# Генерируем у координаты по равномерному распределению и отображаем точки
y3 = np.random.uniform(0, 1, size=points_per_dist)
ax[1,1].scatter( x3, y3, color='#fefe22', s=3)

# Устанавливаем заголовок, сетку и фон
ax[1,1].set_title("Диаграмма рассеяния", fontname='Tahoma', fontsize=14, fontweight='light', fontstyle = 'oblique', color = (0.055, 0.035, 0.286, 0.9))
ax[1,1].grid(True)
ax[1,1].set_facecolor('#000000')

# ===================== [1,2] =====================

# Создаем массив равномерно распределенных чисел в интервале от 0 до 2pi
t = np.linspace(0, 2*np.pi, 1000)
A = 10
B = 3
a = 2.7
b = 10.8
delta = np.pi/4
# Записываем наши функции
x = A * np.sin(a*t + delta)
y = B  * np.sin(b*t)

# Закрашиваем промежуток между функциями, устанавливаем сетку серого цвета и устанавливаем заголовок
ax[1,2].fill_between(x, y, color='#ffb6c1', alpha=0.7)
ax[1,2].grid(True, color='grey')
ax[1,2].set_title("Фигура Лиссажу", fontname='Tahoma', fontsize=14, fontweight='light', fontstyle = 'oblique', color = (0.055, 0.035, 0.286, 0.9))

# Сохраняем фигуру в файле
plt.savefig('result.png')
# Отображаем нашу фигуру на экране
plt.show()