import csv

# Откройте файл для чтения и записи
with open('prices.csv', mode='r', encoding='utf-8') as infile, open('processed_prices.csv', mode='w', newline='', encoding='utf-8') as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)

    # Прочитайте заголовок и запишите его в новый файл
    header = next(reader)
    writer.writerow(header)

    for row in reader:
        # Уберите строку "руб." и пробелы, преобразуйте в число
        price_str = row[0].replace('руб.', '').replace(' ', '')
        price_number = int(price_str)

        # Запишите обработанную цену в новый файл
        writer.writerow([price_number])