import pandas as pd

from config import (
    PLAYER_STATS_FILE,
    CLEAN_PLAYER_STATS_FILE
)

# Only keep the columns we need
COLUMNS = [
    "PLAYER",
    "TEAM",
    "PTS",
    "REB",
    "AST",
    "STL",
    "BLK"
]


def clean_player_data():

    # Read the raw player statistics
    player_stats = pd.read_csv(
        PLAYER_STATS_FILE
    )

    # Keep useful columns only
    clean_data = player_stats[COLUMNS]

    # Remove rows with missing values
    clean_data = clean_data.dropna()

    # Create folder if it doesn't exist
    CLEAN_PLAYER_STATS_FILE.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    # Save the cleaned data
    clean_data.to_csv(
        CLEAN_PLAYER_STATS_FILE,
        index=False
    )

    print(f"Cleaned {len(clean_data)} players")

    return clean_data


if __name__ == "__main__":
    clean_player_data()