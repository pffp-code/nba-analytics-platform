from nba_api.stats.endpoints import leagueleaders

from src.config import PLAYER_STATS_FILE


def fetch_player_stats():

    leaders = leagueleaders.LeagueLeaders(
        season='2025-26'
    )

    df = leaders.get_data_frames()[0]

    print(df.columns.tolist())

    columns = [
        "PLAYER",
        "TEAM",
        "PTS",
        "REB",
        "AST",
        "GP"
    ]

    df = df[columns]

    PLAYER_STATS_FILE.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    df.to_csv(
        PLAYER_STATS_FILE,
        index=False
    )

    print(f"Saved: {PLAYER_STATS_FILE}")

    return df


if __name__ == "__main__":
    fetch_player_stats()