from pathlib import Path

BASE_DIR = Path(__file__).parent.parent

RAW_DATA_DIR = BASE_DIR / "data" / "raw"
PROCESSED_DATA_DIR = BASE_DIR / "data" / "processed"

PLAYER_STATS_FILE = RAW_DATA_DIR / "player_stats.csv"
RANKINGS_FILE = PROCESSED_DATA_DIR / "rankings.csv"

REPORT_FILE = BASE_DIR / "reports" / "ranking_report.txt"

CLEAN_PLAYER_STATS_FILE = (
    PROCESSED_DATA_DIR /
    "clean_player_stats.csv"
)