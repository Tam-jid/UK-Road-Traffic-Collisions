import os

def test_crashes_by_road_class_type_exists():
    """Check if the Crashes by Road Class and Type visualization exists."""
    file_path = "Visualisations/Crashes_by_road_class_type.png"
    assert os.path.isfile(file_path), f"File {file_path} does not exist."
