import os
import pandas as pd
import pandas as pd
data = pd.read_csv('Dataset/Student Depression Dataset.csv')
print(data.head())

def test_file_exists():
    #Test if the dataset file exists
    assert os.path.exists('Dataset/Student Depression Dataset.csv'), "The dataset file is missing."

def test_file_readable():
    #Test if the dataset can be read without errors
    data = pd.read_csv('Dataset/Student Depression Dataset.csv')
    assert data is not None, "The dataset could not be read."

def test_data_not_empty():
    # if the dataset is not empty
    data = pd.read_csv('Dataset/Student Depression Dataset.csv')
    assert len(data) > 0, "The dataset is empty."