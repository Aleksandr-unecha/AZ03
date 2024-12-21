from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import csv

# Укажите путь к вашему ChromeDriver
driver_path = '/path/to/chromedriver'

# Создайте экземпляр веб-драйвера
driver = webdriver.Chrome()

try:
    # Откройте страницу
    driver.get('https://www.divan.ru/bryansk/category/divany-i-kresla')

    # Подождите некоторое время, чтобы страница полностью загрузилась
    time.sleep(5)

    # Найдите все элементы, содержащие цены
    prices = driver.find_elements(By.CSS_SELECTOR, 'span.ui-LD-ZU.KIkOH')

    # Откройте файл для записи
    with open('prices.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)

        # Запишите заголовок
        writer.writerow(['Price'])

        # Запишите цены в файл
        for price in prices:
            writer.writerow([price.text])

finally:
    # Закройте браузер
    driver.quit()