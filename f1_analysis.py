import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Load your CSV file into a DataFrame
file_path = r"C:\Users\juver\OneDrive\F1_Scraper\cleaned_f1_driver_standings_2024.csv"
df = pd.read_csv(file_path)

# Optional: Check if loaded properly
print("Data loaded successfully! Here are the first 5 rows:")
print(df.head())

# --- Now the 8-step analysis ---

# Basic Info About Your Data
print("\nShape (Rows, Columns):", df.shape)
print("\nColumns:\n", df.columns.tolist())
print("\nInfo:")
print(df.info())
print("\nSummary Statistics:")
print(df.describe(include='all'))
print("\nFirst 5 rows:")
print(df.head())

#  Visualize Missing Values
plt.figure(figsize=(15, 6))
sns.heatmap(df.isnull(), cbar=False, cmap="viridis")
plt.title("Missing Values Heatmap")
plt.show()

#  Driver Positions Across Races
position_cols = [col for col in df.columns if col.endswith('_pos')]

df_melted = df.melt(id_vars='Driver', value_vars=position_cols,
                    var_name='Race', value_name='Position')

df_melted['Race'] = df_melted['Race'].str.replace('_pos', '', regex=False)

plt.figure(figsize=(16, 8))
sns.lineplot(data=df_melted, x='Race', y='Position', hue='Driver', marker='o')
plt.gca().invert_yaxis()  # So 1st place is at the top
plt.xticks(rotation=45)
plt.title('Driver Positions Across Races')
plt.xlabel('Race')
plt.ylabel('Finishing Position')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()

#  Average Position Per Driver
avg_positions = df[position_cols].mean(axis=1)

plt.figure(figsize=(12, 6))
sns.barplot(x=avg_positions, y=df['Driver'], palette='mako')
plt.title('Average Finishing Position per Driver')
plt.xlabel('Average Position')
plt.ylabel('Driver')
plt.show()

#  Correlation Between Race Finishes and Points
df_pos_only = df[position_cols].copy()
df_pos_only['Points'] = df['Points']

correlation = df_pos_only.corr()['Points'].drop('Points')

plt.figure(figsize=(12, 6))
correlation.sort_values().plot(kind='barh', color='skyblue')
plt.title('Correlation of Race Finishes with Total Points')
plt.xlabel('Correlation with Points')
plt.show()

#  Outliers in Race Positions
plt.figure(figsize=(16, 6))
sns.boxplot(data=df[position_cols], orient='h', palette='coolwarm')
plt.title('Outliers in Race Positions')
plt.xlabel('Position')
plt.show()

#  Distribution of Total Points
plt.figure(figsize=(10, 5))
sns.histplot(df['Points'], bins=10, kde=True, color='orchid')
plt.title('Distribution of Total Points')
plt.xlabel('Points')
plt.ylabel('Driver Count')
plt.show()

# Spot Suspicious Values (>20 in Positions)
print("\nSuspicious Position Values (>20):")
for col in position_cols:
    high_values = df[col][df[col] > 20]
    if not high_values.empty:
        print(f"\n{col} has strange values:")
        print(high_values)
