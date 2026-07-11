import pandas as pd

from config import (
    CLEAN_PLAYER_STATS_FILE,
    PPI_FILE,
    PPI_WEIGHTS
)

from src.ranking_engine import rank_players


def calculate_ppi():

    # Read the cleaned player data
    player_stats = pd.read_csv(
        CLEAN_PLAYER_STATS_FILE
    )

    # Calculate Player Performance Index (PPI)
    player_stats["PPI"] = (
        player_stats["PTS"] * PPI_WEIGHTS["PTS"]
        + player_stats["REB"] * PPI_WEIGHTS["REB"]
        + player_stats["AST"] * PPI_WEIGHTS["AST"]
        + player_stats["STL"] * PPI_WEIGHTS["STL"]
        + player_stats["BLK"] * PPI_WEIGHTS["BLK"]
    )

    # Round to 2 decimal places
    player_stats["PPI"] = player_stats["PPI"].round(2)

    # Rank players by PPI
    ranked_players = rank_players(
        player_stats,
        "PPI"
    )

    # Create folder if it doesn't exist
    PPI_FILE.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    # Save the result
    ranked_players.to_csv(
        PPI_FILE,
        index=False
    )

    print("PPI calculation completed")

    return ranked_players


if __name__ == "__main__":
    calculate_ppi()