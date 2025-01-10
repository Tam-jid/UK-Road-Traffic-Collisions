import os

def test_yearly_breakdown_exists():
    """Check if the Yearly Breakdown visualization exists."""
    file_path = "Visualisations/Yearly_breakdown.png"
    assert os.path.isfile(file_path), f"File {file_path} does not exist."

