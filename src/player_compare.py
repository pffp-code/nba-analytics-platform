"""
Compare two NBA players.

This module compares two players based on their season statistics.
"""

from pathlib import Path

import pandas as pd

from config import PPI_FILE


def load_player_data():
    """Load processed player statistics."""

    return pd.read_csv(PPI_FILE)


def find_player(df, player_name):
    """Find a player by name."""

    result = df[df["PLAYER"].str.lower() == player_name.lower()]

    if result.empty:
        return None

    return result.iloc[0]


def compare_players(player1, player2):
    """Compare two NBA players."""

    print()
    print("=" * 70)
    print("PLAYER COMPARISON")
    print("=" * 70)

    player1_title = f"{player1['PLAYER']} ({player1['TEAM']})"
    player2_title = f"{player2['PLAYER']} ({player2['TEAM']})"

    print(f"{'Category':<15}{player1_title:<25}{player2_title:<25}")
    print("-" * 70)

    categories = [
        ("Points", "PTS"),
        ("Rebounds", "REB"),
        ("Assists", "AST"),
        ("Steals", "STL"),
        ("Blocks", "BLK"),
        ("PPI", "PPI"),
    ]

    for title, column in categories:

        value1 = player1[column]
        value2 = player2[column]

        if column == "PPI":
            value1 = f"{value1:.1f}"
            value2 = f"{value2:.1f}"
        else:
            value1 = f"{int(value1)}"
            value2 = f"{int(value2)}"

        print(f"{title:<15}{value1:<25}{value2:<25}")

    print("-" * 70)

    if player1["PPI"] >= player2["PPI"]:
        winner = player1["PLAYER"]
    else:
        winner = player2["PLAYER"]

    print(f"Winner (Current PPI): {winner}")

    print()
    print("Summary")
    print("-" * 30)

    summary = []

    if player1["PTS"] > player2["PTS"]:
        summary.append(f"{player1['PLAYER']} scores more points.")
    else:
        summary.append(f"{player2['PLAYER']} scores more points.")

    if player1["REB"] > player2["REB"]:
        summary.append(f"{player1['PLAYER']} grabs more rebounds.")
    else:
        summary.append(f"{player2['PLAYER']} grabs more rebounds.")

    if player1["AST"] > player2["AST"]:
        summary.append(f"{player1['PLAYER']} makes more assists.")
    else:
        summary.append(f"{player2['PLAYER']} makes more assists.")

    summary.append(f"Overall winner: {winner}")

    for line in summary:
        print(f"- {line}")

    save_comparison_report(player1, player2, summary)


def save_comparison_report(player1, player2, summary):
    """Save comparison report."""

    report_path = Path("reports") / "player_compare.txt"

    report_path.parent.mkdir(parents=True, exist_ok=True)

    player1_title = f"{player1['PLAYER']} ({player1['TEAM']})"
    player2_title = f"{player2['PLAYER']} ({player2['TEAM']})"

    categories = [
        ("Points", "PTS"),
        ("Rebounds", "REB"),
        ("Assists", "AST"),
        ("Steals", "STL"),
        ("Blocks", "BLK"),
        ("PPI", "PPI"),
    ]

    with open(report_path, "w", encoding="utf-8") as file:

        file.write("PLAYER COMPARISON\n")
        file.write("=" * 70 + "\n\n")

        file.write(
            f"{'Category':<15}"
            f"{player1_title:<25}"
            f"{player2_title:<25}\n"
        )

        file.write("-" * 70 + "\n")

        for title, column in categories:

            value1 = player1[column]
            value2 = player2[column]

            if column == "PPI":
                value1 = f"{value1:.1f}"
                value2 = f"{value2:.1f}"
            else:
                value1 = f"{int(value1)}"
                value2 = f"{int(value2)}"

            file.write(
                f"{title:<15}"
                f"{value1:<25}"
                f"{value2:<25}\n"
            )

        file.write("-" * 70 + "\n\n")

        file.write("Summary\n")
        file.write("-" * 30 + "\n")

        for line in summary:
            file.write(f"- {line}\n")