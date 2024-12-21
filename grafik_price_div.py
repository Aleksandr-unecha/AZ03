import pandas as pd
import matplotlib.pyplot as plt

# Чтение данных из файла CSV
data = pd.read_csv('processed_prices.csv')

# Предполагаем, что цены хранятся в столбце 'price'
prices = data['Price']

# Построение гистограммы
plt.figure(figsize=(10, 6))
plt.hist(prices, bins=20, color='blue', edgecolor='black')

# Добавление заголовка и меток осей
plt.title('Гистограмма цен')
plt.xlabel('Цена')
plt.ylabel('Частота')

# Показать график
plt.show()