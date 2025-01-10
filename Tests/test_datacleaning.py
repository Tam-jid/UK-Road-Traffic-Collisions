import pandas as pd

def filter_csv():
    df = pd.read_csv('accident_data.csv')

    #filter out rows where 'accident severity' is 'slight'
    filtered_df = df[df['Accident_Severity'] != 'Slight']

    #filter out rows where the road class is empty
    filtered_df = filtered_df[filtered_df['1st_Road_Class'].notna()]

    #filter out rows where there is a special condition at the site
    filtered_df = filtered_df[filtered_df['Special_Conditions_at_Site'].isna()]

    #filter out rows where there is a carriageway hazard, 
    #this is because we do not want any speical circumstances to affect the analysis, 
    #this is also why I removed the 'Special_Conditions_at_Site' as this is accidents where there is something like an oil spill causing the accident
    filtered_df = filtered_df[filtered_df['Carriageway_Hazards'].isna()]

    # Get rid of the 'accident severity' column & 'Carriageway_Hazards' column
    filtered_df = filtered_df.drop(columns=['Accident_Severity'])
    filtered_df = filtered_df.drop(columns=['Carriageway_Hazards'])
    
    # Only include columns needed for analysis
    required_columns = ['1st_Road_Class', 'Date', 'Day_of_Week', 'Junction_Detail', 'Light_Conditions',
                         'Local_Authority_(District)', 'Local_Authority_(Highway)', 'Number_of_Casualties', 'Number_of_Vehicles',
                         'Road_Surface_Conditions', 'Road_Type', 'Speed_limit', 'Time', 'Urban_or_Rural_Area', 'Weather_Conditions']
    filtered_df = filtered_df[required_columns]
    
    return filtered_df

data = filter_csv()
print(data.head())  
filtered_num_rows = data.shape[0]
print(f"The number of rows after filtering is: {filtered_num_rows}")

# Reduce the number of rows in the Dataset to 20,000
reduced_df = data.sample(n=20000, random_state=42)  #use random instead of head(), this is to make sure a fair selection of rows is selected.
data = reduced_df
print(data.shape[0]) #make sure rows is right amount

data.to_csv('filtered_accident_data.csv', index=False) #save the cleaned dataset to a new file



