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

# 3. Distribution of crashes by road class and type

# Combine A(M) with Motorway data as a(m) is a motorway and there is an insignificant amount of incidents
data_modified = data.copy()
data_modified['1st_Road_Class'] = data_modified['1st_Road_Class'].replace('A(M)', 'Motorway')

# Group the modified data
road_class_type_counts = data_modified.groupby(['1st_Road_Class', 'Road_Type']).size().unstack(fill_value=0)

# Sort the data by total crashes
road_class_type_counts['Total'] = road_class_type_counts.sum(axis=1)
road_class_type_counts = road_class_type_counts.sort_values('Total', ascending=True)
road_class_type_counts = road_class_type_counts.drop('Total', axis=1)

sns.set_theme(style="whitegrid")
fig, ax = plt.subplots(figsize=(12, 8))

colors = sns.color_palette("husl", n_colors=len(road_class_type_counts.columns))
road_class_type_counts.plot(kind='barh', stacked=True, ax=ax, color=colors)

# add titles, labels, etc.
plt.title('Distribution of Crashes by Road Class and Type', pad=20, fontsize=14)
plt.xlabel('Number of Crashes', fontsize=12)
plt.ylabel('Road Class', fontsize=12)

# Add exact value labels on the bars
def add_labels(ax, road_class_type_counts):
    for i in range(len(road_class_type_counts.index)):
        total = road_class_type_counts.iloc[i].sum()
        ax.text(total + 100, i, f'Total: {total:,}', 
                va='center', fontsize=10)

add_labels(ax, road_class_type_counts)

# Add legend
plt.legend(title='Road Type', bbox_to_anchor=(1.05, 1), loc='upper left', 
          frameon=True, title_fontsize=12)

# Add gridlines
ax.grid(axis='x', linestyle='--', alpha=0.7)

plt.tight_layout()
plt.savefig('Visualisations/Crashes_by_road_class_type.png', bbox_inches='tight')
#plt.show()
plt.clf()

"""-------------------------------------------------------------------------------"""

# Convert Date to datetime
data['Date'] = pd.to_datetime(data['Date'], format='%d/%m/%Y')

# get the month and day
data['Month'] = data['Date'].dt.month
data['Day'] = data['Date'].dt.day

# Create month-day pairs for December and January
data['MonthDay'] = data['Date'].dt.strftime('%m-%d')

# Filter for December and January only
winter_accidents = data[data['Month'].isin([12, 1])]

# Count accidents by month-day
daily_counts = winter_accidents.groupby('MonthDay').size().reset_index()
daily_counts.columns = ['Date', 'Accidents']

daily_counts['Date'] = pd.to_datetime(daily_counts['Date'], format='%m-%d')
daily_counts = daily_counts.sort_values('Date')

plt.figure(figsize=(12, 6))
plt.plot(range(len(daily_counts)), daily_counts['Accidents'], marker='o')

plt.xticks(range(0, len(daily_counts), 5), 
          daily_counts['Date'].dt.strftime('%b %d')[::5], 
          rotation=45)

plt.title('Daily Accident Counts (December-January)')
plt.xlabel('Date')
plt.ylabel('Number of Accidents')

# Add vertical line for Christmas day
christmas_idx = daily_counts[daily_counts['Date'].dt.strftime('%m-%d') == '12-25'].index
plt.axvline(x=christmas_idx[0], color='r', linestyle='--', label='Christmas')
plt.legend()

plt.grid(True, alpha=0.3)
plt.tight_layout()
#plt.show()
plt.savefig('Visualisations/Christmas_day_crashes.png', bbox_inches='tight')
plt.clf()

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

    # Description for Distribution of Crashes by Road Class and Type
    file.write("Distribution of Crashes by Road Class and Type:\n")
    road_class_type_description = road_class_type_counts.describe()
    file.write(road_class_type_description.to_string())
    file.write("\n\n")

    # Description for Christmas day crashes (December-January)
    file.write("Daily Accident Counts (December-January):\n")
    daily_counts_description = daily_counts.describe()  
    file.write(daily_counts_description.to_string())
    file.write("\n\n")