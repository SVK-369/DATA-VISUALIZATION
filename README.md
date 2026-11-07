# DATA-VISUALIZATION
# data visualization 

1. Loading the Taxis Dataset
2. import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the built-in taxis dataset
df = sns.load_dataset("taxis")
3. 2. Handling Missing Values
# 1. Check missing values
print("Missing values per column:")
print(df.isnull().sum())

# 2. Impute missing values based on column type
# Numerical columns: impute with median
num_cols = df.select_dtypes(include=['float64', 'int64']).columns
for col in num_cols:
    df[col].fillna(df[col].median(), inplace=True)

# Categorical columns: impute with mode
cat_cols = df.select_dtypes(include=['object', 'category']).columns
for col in cat_cols:
    df[col].fillna(df[col].mode()[0], inplace=True)

# 3. For critical columns with missing values where imputation isn't reasonable, drop remaining NaNs
df.dropna(inplace=True)
      Explanation:.isnull().sum() identifies missing counts for each column.   Numerical missing values are replaced with the median (robust against outliers), while categorical fields use the most frequent value (mode).   .dropna() eliminates any remaining unhandled missing values to ensure data integrity.   3. Visualizations using Matplotlib/Pandas Plot
      Line Chart
Plot fare over time using pickup timestamp on the x-axis and fare on the y-axis
Bar Chart
Total fare for each pickup_borough
Pie Chart
Distribution of trips based on payment method.
Histogram
Distribution of trip distance
Box Plot
Distribution of tip amounts for each pickup_borough
4. Visualizations using Seaborn
Count Plot
Number of trips in each pickup_borough.

Python
plt.figure(figsize=(8, 5))
sns.countplot(data=df, x='pickup_borough', palette='Blues_d')
plt.title('Number of Trips by Pickup Borough')
plt.xlabel('Pickup Borough')
plt.ylabel('Trip Count')
plt.show()
Scatter Plot
Relationship between distance (x-axis) and fare (y-axis), colored by pickup_borough.   
1000142741.jpg

Python
plt.figure(figsize=(9, 6))
sns.scatterplot(data=df, x='distance', y='fare', hue='pickup_borough', alpha=0.7)
plt.title('Distance vs Fare by Pickup Borough')
plt.xlabel('Distance')
plt.ylabel('Fare ($)')
plt.show()
Heatmap
Correlation matrix between distance, fare, tip, tolls, and total. 

Python
plt.figure(figsize=(8, 6))
num_cols = ['distance', 'fare', 'tip', 'tolls', 'total']
corr_matrix = df[num_cols].corr()

sns.heatmap(corr_matrix, annot=True, cmap='Blues', fmt='.2f', linewidths=0.5)
plt.title('Correlation Matrix of Numerical Variables')
plt.show()
Pair Plot
Pairwise relationships between distance, fare, tip, and total, colored by pickup_zone (or pickup_borough).   

Python
# Note: Using hue='pickup_borough' for clearer output if pickup_zone has too many unique values
sns.pairplot(df[['distance', 'fare', 'tip', 'total', 'pickup_borough']], hue='pickup_borough', palette='Set2')
plt.show()
Violin Plot
Distribution of fare for each payment method.   
1000142741.jpg

Python
plt.figure(figsize=(8, 5))
sns.violinplot(data=df, x='payment', y='fare', palette='Pastel1')
plt.title('Fare Distribution by Payment Method')
plt.xlabel('Payment Method')
plt.ylabel('Fare ($)')
plt.show()

   
1000142740.jpg
+ 4
