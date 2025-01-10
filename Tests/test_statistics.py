import os

def test_statistics_file_exists():
    """Check if the statistics text file exists."""
    file_path = "Visualisations/Statisticss.txt"
    assert os.path.isfile(file_path), f"File {file_path} does not exist."
