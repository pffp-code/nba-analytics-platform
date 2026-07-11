import pandas as pd


def rank_players(player_stats, column):
    # Sort players from highest to lowest
    ranked_players = player_stats.sort_values(
        by=column,
        ascending=False
    )

    # Reset the index after sorting
    ranked_players = ranked_players.reset_index(
        drop=True
    )

    return ranked_players


def get_top_players(player_stats, column, top_n=10):
    ranked_players = rank_players(
        player_stats,
        column
    )

    return ranked_players.head(top_n)


if __name__ == "__main__":
    print("Ranking Engine")