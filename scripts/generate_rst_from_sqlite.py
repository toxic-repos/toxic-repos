#!/usr/bin/env python3

import typing as t
import sqlite3
from pathlib import Path
from collections import defaultdict
from dataclasses import dataclass

from rst_builder import RSTMaker, RSTBuilder


@dataclass
class DataModel():
    data: str
    name: str
    commit_link: str
    description: str


def main() -> None:
    connection = sqlite3.connect(Path("sqlite/toxic-repos.sqlite3"))
    cursor = connection.cursor()

    data: t.Dict[str, t.List[DataModel]] = defaultdict(list)

    for row in cursor.execute("SELECT * FROM repos ORDER BY problemtype"):
        data[row[2]].append(
            DataModel(
                data=row[1],
                name=row[3],
                commit_link=row[4],
                description=row[5],
            ),
        )
    connection.close()

    result = (
        RSTBuilder(maker=RSTMaker())
        .add_header1(
            "Список проектов с открытым исходным кодом, "
            "содержащих протестное программное обеспечение"
        )
        .add_indents(2)
        .add_create_contents(name="Обзор", depth_level=1)
        .add_indents(2)
    )

    for key, value in data.items():
        result.add_header2(key)
        result.add_indents(1)

        for data_model in value:
            result.add_header3(data_model.name)
            result.add_indents(1)
            result.add_text(
                f"{data_model.data} | "
                f"`Commit <{data_model.commit_link}>`__"
            )
            result.add_indents(2)
            result.add_text(data_model.description)
            result.add_indents(2)

    with open("toxic-repos.rst", "w") as fp:
        fp.write(result.get_result())


if __name__ == "__main__":
    main()
