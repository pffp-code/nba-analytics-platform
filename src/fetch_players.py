from nba_api.stats.endpoints import leagueleaders

from config import PLAYER_STATS_FILE


def fetch_player_statistics():
    # Get the latest NBA player statistics
    leaders = leagueleaders.LeagueLeaders()

    # LeagueLeaders only returns one DataFrame
    player_stats = leaders.get_data_frames()[0]

    # Create folder if it doesn't exist
    PLAYER_STATS_FILE.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    # Save the raw data
    player_stats.to_csv(
        PLAYER_STATS_FILE,
        index=False
    )

    print(f"Downloaded {len(player_stats)} players")

    return player_stats


if __name__ == "__main__":
    fetch_player_statistics()