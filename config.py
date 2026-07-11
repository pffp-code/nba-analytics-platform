"""
config.py

Centralized configuration for the NBA Analytics Platform.

This module stores all project paths and configurable
parameters so that the rest of the application does not
contain hard-coded values.

Author:
Jason

Version:
Phase 2 (v0.2.0)
"""

from pathlib import Path


# ==========================================================
# Project Directories
# ==========================================================

# Root directory of the project.
BASE_DIR = Path(__file__).parent

# Data directories.
DATA_DIR = BASE_DIR / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"

# Report directory.
REPORT_DIR = BASE_DIR / "reports"


# ==========================================================
# CSV Files
# ==========================================================

# Raw player statistics downloaded from nba_api.
PLAYER_STATS_FILE = RAW_DATA_DIR / "player_stats.csv"

# Cleaned player statistics used for analytics.
CLEAN_PLAYER_STATS_FILE = (
    PROCESSED_DATA_DIR / "clean_player_stats.csv"
)

# Final Player Performance Index results.
PPI_FILE = (
    PROCESSED_DATA_DIR / "player_ppi.csv"
)


# ==========================================================
# Reports
# ==========================================================

# Human-readable report.
REPORT_FILE = REPORT_DIR / "top10_ppi_report.txt"


# ==========================================================
# Player Performance Index (PPI)
# ==========================================================

"""
Weight configuration for the Player Performance Index.

The weights represent the relative importance of
different basketball statistics.

Current Formula

PPI =
0.40 × Points
+0.20 × Rebounds
+0.20 × Assists
+0.10 × Steals
+0.10 × Blocks
"""

PPI_WEIGHTS = {
    "PTS": 0.40,
    "REB": 0.20,
    "AST": 0.20,
    "STL": 0.10,
    "BLK": 0.10,
}