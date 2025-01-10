import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns

data = pd.read_csv('Dataset/filtered_accident_data.csv')
print(data.head())

#Visualisations

# 1. Yearly breakdown of accidents and casualties

data['Date'] = pd.to_datetime(data['Date'], format='%d/%m/%Y')
data['Year'] = data['Date'].dt.year

yearly_casualties = data.groupby('Year').agg({
    'Number_of_Casualties': ['count', 'sum']
}).reset_index()
yearly_casualties.columns = ['Year', 'Number_of_Accidents', 'Total_Casualties']
yearly_casualties['Avg_Casualties_per_Accident'] = yearly_casualties['Total_Casualties'] / yearly_casualties['Number_of_Accidents']

# calculate average casualties per accident overall
total_accidents = len(data)
total_casualties = data['Number_of_Casualties'].sum()
avg_casualties = total_casualties / total_accidents

plt.figure(figsize=(12, 6))
sns.set_style('whitegrid')

# Plot bars for number of accidents
ax1 = plt.gca()
ax2 = ax1.twinx()

# Plot bars and line
bars = ax1.bar(yearly_casualties['Year'], yearly_casualties['Number_of_Accidents'], 
               color='skyblue', alpha=0.7, label='Number of Accidents')
line = ax2.plot(yearly_casualties['Year'], yearly_casualties['Avg_Casualties_per_Accident'], 
                color='red', linewidth=2, marker='o', label='Avg Casualties per Accident')

# Add horizontal line for mean casualties 
ax2.axhline(y=avg_casualties, color='green', linestyle='--', linewidth=1.5, 
            label=f'Overall Avg ({avg_casualties:.2f} casualties/accident)')

# Add exact numbers on each bar 
for bar in bars:
    height = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width()/2, height,
             f'{int(height):,}',
             ha='center', va='bottom')

# changing colours etc
ax1.set_xlabel('Year', fontsize=12)
ax1.set_ylabel('Number of Accidents', fontsize=12, color='skyblue')
ax2.set_ylabel('Average Casualties per Accident', fontsize=12, color='red')


plt.title('Road Accidents Trend (2005-2010): Frequency vs Severity', fontsize=14, pad=20)

# Add legend
lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines1 + lines2, labels1 + labels2, loc='upper right')

plt.tight_layout()
plt.savefig('Visualisations/Yearly_breakdown.png', bbox_inches='tight')
#plt.show()
plt.clf()
"""-------------------------------------------------------------------------------"""

# 2. Accidents by hour of the day and day of the week

# Convert Date and time columns to be used
data['Date'] = pd.to_datetime(data['Date'], format='%d/%m/%Y')
data['Time'] = data['Time'].fillna('00:00')  # Fill missing Time values with '00:00'
data['Hour'] = data['Time'].str.split(':').str[0].astype(int)
data['Day_of_Week'] = data['Date'].dt.day_name()

# Create a heatmap for hour of the day (x-axis) and day of the week (y-axis)
plt.figure(figsize=(12, 6))
heatmap_data = pd.crosstab(data['Day_of_Week'], data['Hour'])
sns.heatmap(heatmap_data, cmap='YlGnBu', annot=True, fmt='d', cbar_kws={'label': 'Number of Accidents'})
plt.title('Heatmap of Accidents by Hour and Day of the Week')
plt.xlabel('Hour of the Day')
plt.ylabel('Day of the Week')
plt.tight_layout()
plt.savefig('Visualisations/Accidents_by_hour.png', bbox_inches='tight')
#plt.show()
plt.clf()
"""-------------------------------------------------------------------------------"""

# Text file with statistics (mean,standard deviation, min/max values..)
with open('Visualisations/Statisticss.txt', "w") as file:
    # Description for Yearly Breakdown
    file.write("Yearly Breakdown of Accidents and Casualties:\n")
    yearly_description = yearly_casualties.describe()
    file.write(yearly_description.to_string())
    file.write("\n\n")

    # Description for Heatmap Data (Accidents by Hour and Day of Week)
    file.write("Heatmap of Accidents by Hour and Day of the Week:\n")
    heatmap_description = heatmap_data.describe()
    file.write(heatmap_description.to_string())
    file.write("\n\n")