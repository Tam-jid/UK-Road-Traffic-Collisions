import os

def test_daily_accident_counts_exists():
    """Check if the Christmas day crashes visualisation exists."""
    file_path = "Visualisations/Christmas_day_crashes.png"
    assert os.path.isfile(file_path), f"File {file_path} does not exist."
