import os

def test_daily_accident_counts_exists():
    """Check if the Daily Accident Counts visualisation exists."""
    file_path = "Visualisations/Daily_accident_counts.png"
    assert os.path.isfile(file_path), f"File {file_path} does not exist."
