import numpy as np
import matplotlib.pyplot as plt

# Генерация двух наборов случайных данных
num_points = 100  # количество точек на диаграмме
x = np.random.rand(num_points)
y = np.random.rand(num_points)

# Построение диаграммы рассеяния
plt.scatter(x, y, c='blue', alpha=0.5, marker='o')
plt.title('Диаграмма рассеяния')
plt.xlabel('x')
plt.ylabel('y')

# Показать диаграмму
plt.show()