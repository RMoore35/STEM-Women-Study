import pandas as pd
import matplotlib.pyplot as plt
from IPython.display import display
import seaborn as sns

# Read in data from local csv file, adopted from censuv.gov data
df = pd.read_csv('women-stem.csv')

# Create new column for Gender Majority, used in plotting later
df.loc[df['ShareWomen'] <= .5, 'Gender Majority'] = 'Majority Men'
df.loc[df['ShareWomen'] > .5, 'Gender Majority'] = 'Majority Women'

display(df.head(n=5))

# Initial scatter plot
sns.relplot(x='ShareWomen', y='Median', data=df)
plt.title('Median Salary vs. Share of Women in a Particular Major')
plt.show()

# Add color and shapes based on category for easier visualization
sns.set_palette('Paired', 10)
sns.relplot(x='ShareWomen', y='Median', hue='Major_category',
            style='Major_category', data=df)
plt.title('Median Salary vs Share of Women in a Particular Major')
plt.show()

# Another way to plot the same as above, elimate shapes and alters color based on total
# number of people in a major
sns.relplot(x='ShareWomen', y='Median', hue='Total', data=df)
plt.title('Median Salary vs Share of Women in a Particular Major')
plt.show()

# Incorporate size and color to highlight most popular major
sns.relplot(x='ShareWomen', y='Median', hue='Major_category',
            size='Total', sizes=(15, 200), data=df)
plt.title('Median Salary vs Share of Women in a Particular Major')
plt.show()

# Line plot. Not that useful in this case but used for illustration
sns.relplot(x='ShareWomen', y='Women', kind='line', data=df)
plt.title('Share of Women vs Total Women in a Particular Major')
plt.show()

# Regression line fit to plot
sns.lmplot(x='ShareWomen', y='Median', data=df)
plt.show()

# Plot using categorical variables for x
sns.catplot(x='Major_category', y='Median', data=df)
plt.xticks(rotation=90)
plt.show()

# Investigating both majority men/women and median salaries
sns.catplot(x='Major_category', y='Median', kind='swarm',
            data=df)
plt.xticks(rotation=90)
plt.show()

# Box plot
sns.catplot(x='Major_category', y='Median', kind='box', data=df)
plt.xticks(rotation=90)
plt.show()

# Boxen Plot
sns.catplot(x='Major_category', y='Median', kind='boxen',
            data=df)
plt.title('Boxen Plot')
plt.xticks(rotation=90)
plt.show()

# Violin Plot
sns.catplot(x='Major_category', y='Median', kind='violin',
            data=df)
plt.title('Violin Plot')
plt.xticks(rotation=90)
plt.show()

# Violin plot with majority men/women shown
sns.catplot(x='Major_category', y='Median', kind='violin',
            hue='Gender Majority', split='True', data=df)
plt.xticks(rotation=90)
plt.show()

# Final chart: bar chart
sns.catplot(x='Major_category', kind='count', data=df)
plt.xticks(rotation=90)
plt.show()
