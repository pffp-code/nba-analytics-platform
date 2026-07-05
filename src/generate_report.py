import pandas as pd

from tabulate import tabulate

from src.config import (
    REPORT_FILE,
    RANKINGS_FILE
)


def generate_report():

    df = pd.read_csv(
        RANKINGS_FILE
    )

    top10 = df.head(10)

    report = tabulate(
        top10,
        headers="keys",
        tablefmt="grid",
        showindex=False
    )

    REPORT_FILE.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    with open(
        REPORT_FILE,
        "w",
        encoding="utf-8"
    ) as f:
        f.write(report)

    print(report)


if __name__ == "__main__":
    generate_report()