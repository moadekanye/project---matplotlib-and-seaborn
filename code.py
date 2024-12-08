import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
data = pd.read_csv('diabetes_012_health_indicators_BRFSS2015.csv')

# Preview the data
print(data.head())
print(data.info())

# Countplot for diabetes status
# Visualizing the distribution of diabetes status.
plt.figure(figsize=(8, 5))
sns.countplot(x='Diabetes_012', data=data, palette='pastel')
plt.title('Distribution of Diabetes Status', fontsize=14)
plt.xlabel('Diabetes Status (0=No, 1=Pre, 2=Yes)', fontsize=12)
plt.ylabel('Count', fontsize=12)
plt.show()

# Calculate correlations
# Correlation matrix of health indicators
correlation_matrix = data.corr()

# Plot heatmap
plt.figure(figsize=(12, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Heatmap of Health Indicators', fontsize=16)
plt.show()

# Examines how key indicators differ by diabetes status
plt.figure(figsize=(8, 6))
sns.boxplot(x='Diabetes_012', y='HighBP', data=data, palette='pastel')
plt.title('High Blood Pressure vs Diabetes Status', fontsize=14)
plt.xlabel('Diabetes Status (0=No, 1=Pre, 2=Yes)', fontsize=12)
plt.ylabel('High Blood Pressure (0=No, 1=Yes)', fontsize=12)
plt.show()

# Visualize relationships between continuous variables
plt.figure(figsize=(8, 6))
sns.scatterplot(x='PhysActivity', y='HighChol', hue='Diabetes_012', data=data, palette='viridis')
plt.title('Physical Activity vs High Cholesterol', fontsize=14)
plt.xlabel('Physical Activity (0=No, 1=Yes)', fontsize=12)
plt.ylabel('High Cholesterol (0=No, 1=Yes)', fontsize=12)
plt.legend(title='Diabetes Status')
plt.show()

# Shows diabetes prevalence by education level.
plt.figure(figsize=(8, 6))
sns.barplot(x='Education', y='Diabetes_012', data=data, palette='coolwarm')
plt.title('Education Levels and Diabetes Prevalence', fontsize=14)
plt.xlabel('Education Level (1=Lowest, 5=Highest)', fontsize=12)
plt.ylabel('Average Diabetes Status', fontsize=12)
plt.show()

# Explore the relationships among multiple health indicators
selected_columns = ['HighBP', 'HighChol', 'BMI', 'PhysActivity', 'Income', 'Diabetes_012']
sns.pairplot(data[selected_columns], hue='Diabetes_012', palette='Set2')
plt.suptitle('Pairplot of Health Indicators by Diabetes Status', y=1.02, fontsize=16)
plt.show()
