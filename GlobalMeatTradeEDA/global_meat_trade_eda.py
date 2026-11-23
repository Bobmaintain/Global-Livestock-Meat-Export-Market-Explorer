import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

np.random.seed(77)

#1. Simulate a clean 10-year FADSTAT poultry & Dairy Export Dataset (Tonnes)
countries = ['Ireland', 'Germany', 'Netherlands', 'United Kingdom', 'Brazil','United States', 'Saudi Arabia', 'Kuwait']
years = list(range(2016, 2026))

rows = []
for country in countries:
    base_volume = np.random.randint(150000, 900000)
    growth_trend = np.random.uniform(1.01, 1.06)  # 1% to 6% annual growth
    for i, year in enumerate(years):
        vol = int(base_volume * (growth_trend ** i) + np.random.uniform(0.96, 1.04))
        rows.append({'Country': country, 'Year': year, 'Export_Volume_Tonnes': vol})

df = pd.DataFrame(rows)

#2. Calculate Year-over-Year (YoY) Growth
df = df.sort_values(['Country', 'Year'])
df['YoY_Growth_Pct'] = np.round(df.groupby('Country')['Export_Volume_Tonnes'].pct_change() * 100, 2)

print("--- LATEST YEAR (2025) EXPORT STANDING ---")
print(df[df['Year'] == 2025].sort_values('Export_Volume_Tonnes', ascending=False).to_string(index=False))

# 3. Create Pivot Table and Heatmap
pivot_df = df.pivot(index='Country', columns='Year', values='Export_Volume_Tonnes') / 1000 # Convert to Thousands of Tonnes

plt.figure(figsize=(12, 7))
sns.heatmap(pivot_df, annot=True, fmt=".0f", cmap="YlGnBu", cbar_kws={'label': 'Export Volume (Thousands of Tonnes)'})
plt.title('10-Year Global Animal Protein Export Trends (2016-2025)')
plt.xlabel('Year')
plt.ylabel('Exporting Nation')
plt.tight_layout()
plt.savefig('global_meat_trade_heatmap.png')
print("\nHeatmap saved as 'global_meat_trade_heatmap.png'.")
