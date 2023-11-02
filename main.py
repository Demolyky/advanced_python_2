import csv

# Открываем файл CSV и читаем данные
with open('phonebook_raw.csv', 'r', encoding='utf-8') as csvfile:
    # Создаем объект csv.reader для чтения данных из файла, указываем ',' как разделитель
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Пропускаем заголовок (первую строку) файла
    next(csvreader)
    
    # Читаем данные из каждой строки и выводим их
    for row in csvreader:
        lastname = row[0]
        firstname = row[1]
        surname = row[2]
        organization = row[3]
        position = row[4]
        phone = row[5]
        email = row[6]
        print(f'Фамилия: {lastname}, Имя: {firstname}, Отчество: {surname}, Организация: {organization}, Должность: {position}, Телефон: {phone}, Email: {email}')
