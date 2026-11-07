#DATA VISUALIZATION
#Loading the Taxis Dataset
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the built-in taxis dataset
df = sns.load_dataset("taxis")

#2. Handling Missing Values
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

#3. Visualizations using Matplotlib/Pandas Plot
# Convert pickup column to datetime format
df['pickup'] = pd.to_datetime(df['pickup'])

# Sort by pickup time for smooth plotting
df_sorted = df.sort_values('pickup')

plt.figure(figsize=(10, 5))
plt.plot(df_sorted['pickup'], df_sorted['fare'], color='skyblue', linewidth=1)
plt.title('Fare Over Time')
plt.xlabel('Pickup Timestamp')
plt.ylabel('Fare ($)')
plt.grid(True)
plt.show()

#Bar Chart
# Group data by pickup_borough and calculate total fare
fare_by_borough = df.groupby('pickup_borough')['fare'].sum()

plt.figure(figsize=(8, 5))
fare_by_borough.plot(kind='bar', color='skyblue', edgecolor='black')
plt.title('Total Fare by Pickup Borough')
plt.xlabel('Pickup Borough')
plt.ylabel('Total Fare ($)')
plt.xticks(rotation=0)
plt.grid(axis='y')
plt.show()

#Pie Chart
payment_counts = df['payment'].value_counts()

plt.figure(figsize=(6, 6))
plt.pie(payment_counts, labels=payment_counts.index, autopct='%1.1f%%', colors=['skyblue', 'lightgreen'], startangle=90)
plt.title('Trip Distribution by Payment Method')
plt.show()

#Histogram
plt.figure(figsize=(8, 5))
plt.hist(df['distance'], bins=30, color='skyblue', edgecolor='black')
plt.title('Distribution of Trip Distance')
plt.xlabel('Distance (miles)')
plt.ylabel('Frequency')
plt.grid(axis='y')
plt.show()

#Box Plot
plt.figure(figsize=(8, 5))
df.boxplot(column='tip', by='pickup_borough', grid=True)
plt.title('Tip Distribution by Pickup Borough')
plt.suptitle('') # Suppress auto-generated title
plt.xlabel('Pickup Borough')
plt.ylabel('Tip ($)')
plt.show()

#4. Visualizations using Seaborn
#count plot
plt.figure(figsize=(8, 5))
sns.countplot(data=df, x='pickup_borough', palette='Blues_d')
plt.title('Number of Trips by Pickup Borough')
plt.xlabel('Pickup Borough')
plt.ylabel('Trip Count')
plt.show()

#Scatter Plot

plt.figure(figsize=(9, 6))
sns.scatterplot(data=df, x='distance', y='fare', hue='pickup_borough', alpha=0.7)
plt.title('Distance vs Fare by Pickup Borough')
plt.xlabel('Distance')
plt.ylabel('Fare ($)')
plt.show()

#Heatmap
plt.figure(figsize=(8, 6))
num_cols = ['distance', 'fare', 'tip', 'tolls', 'total']
corr_matrix = df[num_cols].corr()

sns.heatmap(corr_matrix, annot=True, cmap='Blues', fmt='.2f', linewidths=0.5)
plt.title('Correlation Matrix of Numerical Variables')
plt.show()

#Pair Plot
plt.figure(figsize=(9, 6))
sns.scatterplot(data=df, x='distance', y='fare', hue='pickup_borough', alpha=0.7)
plt.title('Distance vs Fare by Pickup Borough')
plt.xlabel('Distance')
plt.ylabel('Fare ($)')
plt.show()

#Violin Plot
plt.figure(figsize=(8, 5))
sns.violinplot(data=df, x='payment', y='fare', palette='Pastel1')
plt.title('Fare Distribution by Payment Method')
plt.xlabel('Payment Method')
plt.ylabel('Fare ($)')
plt.show()
