from src.fetch_players import (
    fetch_player_stats
)

from src.build_rankings import (
    build_rankings
)

from src.generate_report import (
    generate_report
)


def main():

    print("=== Phase 1 ===")

    print("Fetching NBA data...")
    fetch_player_stats()

    print("Building rankings...")
    build_rankings()

    print("Generating report...")
    generate_report()

    print("Done.")


if __name__ == "__main__":
    main()