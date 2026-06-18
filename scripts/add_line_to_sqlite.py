import argparse
import re
import sqlite3
import os
from datetime import datetime

database_path = '../data/sqlite/toxic-repos.sqlite3'  # Путь к базе данных SQLite


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Пример программы для работы с аргументами через args.")
    parser.add_argument("--name",
                        type=str,
                        required=True,
                        help="Имя репозитория в формате ИМЯ_ОРГАНИЗАЦИИ/ИМЯ_РЕПОЗИТОРИЯ, пример: medikoo/es5-ext")
    parser.add_argument("--datetime",
                        type=str,
                        required=False,
                        help="Дата обнаружения в формате ГГГГ-ММ-ДД ЧЧ:ММ:СС")
    parser.add_argument("--problem_type",
                        type=str,
                        required=True,
                        choices=["broken_assembly", "ddos", "hostile_actions", "ip_block", "malware", "polical_slogans"],
                        help="Тип проблемы. Возможные значения: broken_assembly, ddos, hostile_actions, ip_block, malware, polical_slogans.")
    parser.add_argument("--commit_link",
                        type=str,
                        required=True,
                        help="Гиперссылка на git-коммит подтверждающая факт внесения вредоносных изменений, пример: https://github.com/medikoo/es5-ext/commit/28de285ed433b45113f01e4ce7c74e9a356b2af2")
    parser.add_argument("--description",
                        type=str,
                        required=True,
                        help="Обоснование внесение записи с указанием выявленных вредоносных фактов")
    parser.add_argument("--purl",
                        type=str,
                        required=False,
                        help="Идентификатор пакета в формате PURL")
    parser.add_argument("--purl_link",
                        type=str,
                        required=False,
                        help="Гиперссылка на пакет на сайте пакетного менеджера")
    args = parser.parse_args()

    # Проверка существования файлов
    if not os.path.exists(database_path):
        print(f"Файл базы данных {database_path} не найден!")
        exit(1)
    if not re.fullmatch(r'^(https?://)?github\.com/[\w\d_-]+/[\w\d_-]+/commit/[\w\d]+$', args.commit_link):
        print("--commit_link не соответствует пример: https://github.com/ORG_NAME/REPO_NAME/commit/COMMIT_SHA, пример: https://github.com/medikoo/es5-ext/commit/28de285ed433b45113f01e4ce7c74e9a356b2af2")
        exit(1)
    if not re.fullmatch(r'^[\w\d_-]+/[\w\d_-]+$', args.name):
        print("--name не соответствует ORG_NAME/REPO_NAME, пример: medikoo/es5-ext")
        exit(1)

    conn = sqlite3.connect(database_path)  # Подключение к базе данных
    cursor = conn.cursor()

    # Получаем текущий самый большой id в базе
    cursor.execute("SELECT MAX(id) AS max_id FROM repos;")
    result = cursor.fetchone()
    max_id: int = -1
    if result:
        max_id = result[0]
    if max_id > 0:
        max_id = max_id + 1
        print(f"Номер записи будет: {max_id}")
    else:
        print("Не удалось получить самый большой id из таблицы repos")
        exit(1)
    if not args.datetime:
        current_datetime = datetime.now()
        args.datetime = current_datetime.strftime('%Y-%m-%d %H:%M:%S')
        print(f"Дата обнаружения заменена на {args.datetime}")

    # Вносим запись если корректна
    try:
        sql_query = """
                    INSERT INTO repos (id, datetime, problem_type, name, commit_link, description, "PURL-link", PURL)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                """
        data = (
            max_id,  # Обновленный id
            args.datetime,
            args.problem_type,
            args.name,
            args.commit_link,
            args.description,
            args.purl_link,
            args.purl
        )
        cursor.execute(sql_query, data)
        conn.commit()
        print("Данные успешно импортированы!")
    except sqlite3.Error as e:
        print(f"Ошибка работы с базой данных: {e}")
    finally:
        conn.close()
