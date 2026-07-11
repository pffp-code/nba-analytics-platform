from src.fetch_players import fetch_player_statistics
from src.data_cleaner import clean_player_data
from src.ppi import calculate_ppi
from src.report_generator import generate_ppi_report


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


if __name__ == "__main__":
    main()