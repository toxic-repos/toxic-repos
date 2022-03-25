import sys
import sqlite3
import json

infile = "../toxic-repos.txt"
outfile = "../toxic-repos.json"
# output JSON format (array of dicts):
#[
#  {
#    "datetime": "dd.mm.yyyy hh:MM",
#    "problemtype": "type",
#    "productname": "product",
#    "url": "url",
#    "comment": "human-readable comment"
#  },
#]


TABLE_CREATION_QUERY = """
    CREATE TABLE IF NOT EXISTS "repos" (
	"id"	INTEGER,
	"datetime"	TEXT,
	"problemtype"	TEXT,
	"productname"	TEXT,
	"url"	TEXT,
	"comment"	TEXT,
	PRIMARY KEY("id" AUTOINCREMENT)
);
"""


toxics_array = []
fields = ["datetime", "problemtype", "productname", "url", "comment"]
with open(infile, 'r', encoding='utf-8') as fh:
    print("Читаем txt файл", file=sys.stderr)
    # not using `logging` or `loguru` module to avoid need for dependency
    for line in fh:
        description = list(line.strip().split('\t', 4))
        print(f'Прочитана и распознана строка: {description}', file=sys.stderr)
        toxics_array.append(dict(zip(fields, description)))

with open(outfile, 'w', encoding='utf-8') as out_file:
    print("Пишем json файл", file=sys.stderr)
    json.dump(toxics_array, out_file, indent=2)

db = None # default value for case when DB failde to be opened
try:
    print("Соединяемся с SQLite базой", file=sys.stderr)
    db = sqlite3.connect("../sqlite/toxic-repos.sqlite3")
    c = db.cursor()
    c.execute(TABLE_CREATION_QUERY)
    for one_txc in toxics_array:
        insert_query = f"""
            INSERT INTO repos
            ({','.join(fields)})
            VALUES (?, ?, ?, ?, ?);
            """
        ins_data = tuple([one_txc[k] for k in fields])
        c.execute(insert_query, ins_data)
except sqlite3.Error as error:
    print(f"Ошибка при работе с SQLite базой: {error}", file=sys.stderr)
finally:
    if db:
        db.commit()
        print("Записи успешно вставлены в таблицу.", file=sys.stderr)
        db.close()
        print("Соединение с SQLite закрыто", file=sys.stderr)
