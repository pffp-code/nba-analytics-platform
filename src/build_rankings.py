import pandas as pd

from src.config import (
    PLAYER_STATS_FILE,
    RANKINGS_FILE
)


def build_rankings():

    df = pd.read_csv(
        PLAYER_STATS_FILE
    )

    rankings = df.sort_values(
        by="PTS",
        ascending=False
    )

    RANKINGS_FILE.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    rankings.to_csv(
        RANKINGS_FILE,
        index=False
    )

    return rankings


if __name__ == "__main__":
    build_rankings()