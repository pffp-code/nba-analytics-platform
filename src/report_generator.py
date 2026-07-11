import pandas as pd
from tabulate import tabulate

from config import (
    PPI_FILE,
    REPORT_FILE
)


def generate_ppi_report():

    # Read the PPI results
    player_stats = pd.read_csv(
        PPI_FILE
    )

    # Get the top 10 players
    top_players = player_stats.head(10)

    # Convert the DataFrame into a table
    report = tabulate(
        top_players,
        headers="keys",
        tablefmt="grid",
        showindex=False,
        floatfmt=".2f"
    )

    # Create folder if it doesn't exist
    REPORT_FILE.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    # Save the report
    with open(
        REPORT_FILE,
        "w",
        encoding="utf-8"
    ) as file:
        file.write(report)

    print(report)

    print(f"\nReport saved to {REPORT_FILE}")


if __name__ == "__main__":
    generate_ppi_report()