# Импортируем библиотеки для работы с графиками и массивами
import matplotlib.pyplot as plt
import matplotlib.cbook as cbook
import numpy as np

# Создаем фигуру с сеткой 2х3. Задаем ей ширину и высоту
fig, ax = plt.subplots(2, 3, figsize=(16, 12))
fig.set_figwidth(9)
fig.set_figheight(7)

# Настраиваем оси для каждой клетки. У оси убираем, так как там картинка
ax[0,0].axis('off')
ax[0,1].tick_params(axis='both', labelsize=12, rotation=45,  labelfontfamily='Comic Sans MS')
ax[0,2].tick_params(axis='both', labelsize=12, rotation=45,  labelfontfamily='Comic Sans MS')
ax[1,0].tick_params(axis='both', labelsize=12, rotation=45,  labelfontfamily='Comic Sans MS')
ax[1,1].tick_params(axis='both', labelsize=12, rotation=45,  labelfontfamily='Comic Sans MS')
ax[1,2].tick_params(axis='both', labelsize=12, rotation=45,  labelfontfamily='Comic Sans MS')

# Загружаем файл с картинкой и устанавливаем его в первую клетку. Устанавливаем заголовок в соответствии с заданием
with cbook.get_sample_data('C:\\Users\\fishi\\PycharmProjects\\python_laboratory_work\\png.jpg') as image_file:
       image = plt.imread(image_file)
ax[0,0].imshow(image)
ax[0,0].set_title("Кот", fontname='Tahoma', fontsize=14, fontweight='light', fontstyle = 'oblique', color = (0.055, 0.035, 0.286, 0.9))

# Построчно считываем из файла с данными и записываем строки в список
data = []
with open("data.txt") as file:
       for line in file:
              # Разделение строки на части по пробелам и преобразование каждой части во float
              data.append([float(x) for x in line.split()])

# Преобразуем первую строку и девятую в массивы NumPy
x = np.array(data[0])
y = np.array(data[8])

# Заливаем цветом области выше и ниже нуля
ax[0,1].fill_between(x, y,  where=(y<0), color='#00bfff', alpha=0.7)
ax[0,1].fill_between(x, y, where=(y>0), color='#ffa8af', alpha=0.7)
# Устанавливаем заголовок и включаем отображение сетки
ax[0,1].set_title("График", fontname='Tahoma', fontsize=14, fontweight='light', fontstyle = 'oblique', color = (0.055, 0.035, 0.286, 0.9))
ax[0,1].grid(True)

# Отображаем нашу фигуру на экране
plt.show()