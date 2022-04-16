#!/usr/bin/env python3

import typing as t
import sqlite3
import json
import csv
from pathlib import Path

DATABASE_PATH = Path("data/sqlite/toxic-repos.sqlite3")

JSON_OUTFILE_PATH = Path("data/json/toxic-repos.json")
CSV_OUTFILE_PATH = Path("data/csv/toxic-repos.csv")


def main() -> None:
    connection = sqlite3.connect(DATABASE_PATH)
    cursor = connection.cursor()

    execute_result = cursor.execute("SELECT * FROM repos ORDER BY problem_type")

    column_datas: t.List[t.Tuple[t.Any, ...]] = list(execute_result)  # type: ignore
    row_names = list(map(lambda x: x[0], cursor.description))

    # To json
    json_data = [
        {
            row_names[index]: data
            for index, data in enumerate(column_data)
        }
        for column_data in column_datas
    ]
    with open(JSON_OUTFILE_PATH, "w") as fp:
        json.dump(json_data, fp, ensure_ascii=False, indent=4)

    # To csv
    with open(CSV_OUTFILE_PATH, "w", newline='') as fp:
        csv_writer = csv.writer(fp)
        csv_writer.writerow(row_names)
        for column_data in column_datas:
            csv_writer.writerow(column_data)


if __name__ == "__main__":
    main()
