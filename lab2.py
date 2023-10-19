from csv import reader


#1
flag = 0
count = 0
output = open("result.txt", "w")
search = input("Search for: ")
with open("books-en.csv", "r") as books:
    table = reader(books, delimiter=";")
    for row in list(table)[1:]:
        if len(row[1]) >= 30:
            count += 1
    print("Задание 1. Количество записей, в которых азвание длиннее 30 символов: ", count)


#2
with open('books-en.csv', 'r') as csvfile:
    table = reader(csvfile, delimiter=';')
    for row in list(table)[1:]:
        lower_case = row[2].lower()
        index = lower_case.find(search.lower())
        if index != -1:
            if int(float(row[6].replace(",", "."))) >= 200:
                flag = 1
                print("Задание 2: ", row[1], row[2])
    if flag == 0:
        print("Задание 2: Цена <= 200")


#3
number = 0
with open('books-en.csv', 'r') as csvfile:
    table = reader(csvfile, delimiter=';')
    for row in list(table)[50:70]:
        number += 1
        output.write(f'{number}. {row[2]}. {row[1]}. {row[3]}.\n')

output.close()