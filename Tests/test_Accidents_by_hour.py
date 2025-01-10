import os

def test_accidents_by_hour_exists():
    """Check if the Accidents by Hour visualization exists."""
    file_path = "Visualisations/Accidents_by_hour.png"
    assert os.path.isfile(file_path), f"File {file_path} does not exist."
