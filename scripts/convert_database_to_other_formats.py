#!/usr/bin/env python3

import typing as t
import sqlite3
import json
import csv
from pathlib import Path
from dataclasses import dataclass


DATABASE_PATH = Path("data/sqlite/toxic-repos.sqlite3")

JSON_OUTFILE_PATH = Path("data/json/toxic-repos.json")
CSV_OUTFILE_PATH = Path("data/csv/toxic-repos.csv")


def main() -> None:
    connection = sqlite3.connect(DATABASE_PATH)
    cursor = connection.cursor()

    database_data: t.List[t.Dict[str, t.Any]] = []

    for row in cursor.execute("SELECT * FROM repos ORDER BY problem_type"):
        database_data.append(
            dict(
                datetime=row[1],
                problem_type=row[2],
                name=row[3],
                commit_link=row[4],
                description=row[5],
            ),
        )

    # To json
    with open(JSON_OUTFILE_PATH, "w") as fp:
        json.dump(database_data, fp, ensure_ascii=False, indent=4)

    # To csv
    with open(CSV_OUTFILE_PATH, "w") as fp:
        csv_writer = csv.writer(fp)
        csv_writer.writerow(
            ["datetime", "problem_type", "name", "commit_link", "description"],
        )
        for row in database_data:
            csv_writer.writerow(row.values())


if __name__ == "__main__":
    main()
