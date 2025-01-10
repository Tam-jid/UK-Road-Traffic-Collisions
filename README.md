# Analysing car accidents trends UK

--- 

## 1. Overview

This repository contains visualisation figures of a dataset about car accidents that occur in the UK. The dataset used contains several factors at the time of each incident, including police force information and crash severity. 
From this, I have analysed the trends in accidents through time of day, road classification, road type and casualties. This analysis was done in hopes of finding patterns and reasons as to why or when accidents occur on UK roads and what can be done about this.

The hypothesis tested is: The number of accidents varies evenly across different road types and conditions, with the volume of accidents being most affected by the time of day.  

## 2. Repository structure 
- ** .circleci/: Config.yml file to allow for CircleCI integration for testing at each commit
- **`Dataset/`: Cleaned version of data. 
- ** `Tests/`: All test files ran by CircleCI at each commit
- ** `Visualisations/`: All visualisations used in the analysis
- ** `gitignore`: Specifies files to be ignored by git. Original raw dataset is placed here due to excessive file size.
- ** `analysis.py`: Python script for all data analysis and visualisations.
- ** `datacleaning.py`: Python script for cleaning dataset. Not included in Tests/ folder as original dataset too large to be pushed to github.
- ** `requirements.txt`: Python dependencies needed to run the analysis

## 3. Dataset

The dataset was sourced from the Open Data website of the UK government, where the information has been published by the Department of Transport. Data is collated in kaggle with a usability rating of 10.00.

**Size**: Over 2 million rows and 34 columns before cleaning 
**Cleaning process**: Filtered data for analysis, removed empty values and dropped unnecessary columns that would not be used in analysis

The dataset includes accident dates, casualties, vehicles involved. As well as other information on the conditions at the time, the road/junction details etc.

A large amount of columns were discarded for the purpose of the analysis. Such as the emission of special conditions at the site of a crash. This includes things like oil spills on the road. I have removed this because I am trying to analyse other factors and including special conditions would skew results. I also took out any cases where there was anything blocking the road as normal, such as pedestrians or roadworks. Again, this is due to the analysis focusing on 'normal' circumstances.

## 4. Dataset size issues

Due to a dataset file size of over 100mb (286mb), the original raw dataset cleaned in python could not be commited continously to Github. Attached is a link to where the dataset can be found, which can be used if running the dataset cleaning script. https://www.kaggle.com/datasets/salmankhaliq22/road-traffic-collision-dataset

## 5. Running instructions

To run the analysis:
1. Clone the repository:
   ```bash
   git clone https://github.com/Tam-jid/UK-Road-Traffic-Collisions.git
   cd UK-Road-Traffic-Collisions
 2. Install the required dependencies from 'requirements.txt':
    ```bash
    pip install -r requirements.txt

4. Run the data analysis script - 'analysis.py':
   ```bash
   python data_analysis.py

6. To execute the test suite:
    ```bash
    pytest tests/

7. View the visualisations:

   Navigate inside the 'Visualisations/' folder to see png files of the visualisations made.

