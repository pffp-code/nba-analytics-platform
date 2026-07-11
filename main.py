from src.fetch_players import fetch_player_statistics
from src.data_cleaner import clean_player_data
from src.ppi import calculate_ppi
from src.report_generator import generate_ppi_report
from src.player_compare import (
    load_player_data,
    find_player,
    compare_players,
)


def main():

    print("NBA Analytics Platform")
    print("-" * 30)

    # Step 1: Download player statistics
    fetch_player_statistics()

    # Step 2: Clean the data
    clean_player_data()

    # Step 3: Calculate Player Performance Index
    calculate_ppi()

    # Step 4: Generate the final report
    generate_ppi_report()

    print("\nDone!")

    print("\nPlayer Comparison")
    print("-" * 30)

    df = load_player_data()

    player1_name = input("First player : ")
    player2_name = input("Second player: ")

    player1 = find_player(df, player1_name)
    player2 = find_player(df, player2_name)

    if player1 is None:
        print(f"\nCannot find player: {player1_name}")
        return

    if player2 is None:
        print(f"\nCannot find player: {player2_name}")
        return

    print()
    compare_players(player1, player2)


if __name__ == "__main__":
    main()