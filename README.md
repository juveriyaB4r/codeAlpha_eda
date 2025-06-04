# CodeAlpha - Exploratory Data Analysis on F1 2024 Standings

This project performs Exploratory Data Analysis (EDA) on the cleaned 2024 Formula 1 driver standings dataset. The goal is to identify trends, insights, and patterns from the season’s data.

#Files
- `f1_analysis.py` → Full EDA script with visualizations
- (You can optionally add `cleaned_f1_driver_standings_2024.csv` here as well)

# Tools Used
- `pandas`
- `matplotlib`
- `seaborn`

#Key EDA Steps Performed
1. Dataset shape, columns, types, summary statistics
2. Missing value heatmap
3. Line plot of driver positions across races
4. Bar chart for average finishing position per driver
5. Correlation analysis between race positions and total points
6. Boxplots to identify outliers in positions
7. Histogram showing distribution of total points
8. Detection of suspicious position values (e.g., >20)

#Sample Insights
- The best drivers had low average positions across all races.
- Some races showed clear anomalies or outlier placements.
- There’s a strong negative correlation between position (lower = better) and final points.
- Points distribution is highly skewed toward top-performing drivers.

# Dataset Used
- `cleaned_f1_driver_standings_2024.csv` (from Task 1 – Web Scraping & Cleaning)
