import sqlite3
import json

infile = "../toxic-repos.txt"
outfile = "../toxic-repos.json"

dict1 = {}
fields = ["datetime", "problemtype", "productname", "url", "comment"]
with open(infile, 'r', encoding='utf-8') as fh:
    print("Читаем txt файл")
    l = 1

    for line in fh:
        description = list(line.strip().split('\t', 4))

        print(description)

        sno = str(l)

        i = 0
        dict2 = {}
        while i < len(fields):
            dict2[fields[i]] = description[i]
            i = i + 1

        dict1[sno] = dict2
        l = l + 1

out_file = open(outfile, 'w', encoding='utf-8')
json.dump(dict1, out_file, indent='\t')
print("Пишем json файл")
out_file.close()

traffic = json.load(open('../toxic-repos.json'))
print("Читаем json файл")

try:
    db = sqlite3.connect("../sqlite/toxic-repos.sqlite3")
    print("Соединяемся с SQLite базой")
    query = "insert into repos values (?, ?, ?, ?, ?, ?)"
    columns = ['datetime', 'problemtype', 'productname', 'url', 'comment']
    for datetime, data in traffic.items():
        keys = (datetime,) + tuple(data[c] for c in columns)
        c = db.cursor()
        c.execute(query, keys)
except sqlite3.Error as error:
    print("Ошибка при работе с SQLite базой", error)
finally:
    if db:
        db.commit()
        print("Записи успешно вставлены в таблицу.")
        db.close()
        print("Соединение с SQLite закрыто")
