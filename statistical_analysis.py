# -*- coding: utf-8 -*-
"""statistical_analysis.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1i6bOhNj-99BzAXK5FgY2t6lXe5afok_1
"""

from google.colab import files

# Upload files
uploaded = files.upload()

import pandas as pd

# Load the datasets
train_data = pd.read_csv('loan-train.csv')
test_data = pd.read_csv('loan-test.csv')

# Display the first few rows of the training data
print(train_data.head())

#HYBRID MODEL FOR DESCRIPTIVE ANALYSIS
# Import necessary libraries
from google.colab import files
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Upload the files
uploaded = files.upload()

# Step 2: Load the datasets into pandas DataFrames
train_data = pd.read_csv('loan-train.csv')
test_data = pd.read_csv('loan-test.csv')

# Step 3: Verify the data and data types
print("Training Data:")
print(train_data.head())
print("\nData Types:")
print(train_data.dtypes)

# Step 4: Convert LoanAmount to numeric, errors='coerce' will turn non-numeric to NaN
train_data['LoanAmount'] = pd.to_numeric(train_data['LoanAmount'], errors='coerce')

# Check for any NaNs created in LoanAmount
print("\nChecking for NaN values in LoanAmount:")
print(train_data['LoanAmount'].isna().sum())

# Step 5: Data Visualization
# Set styles for seaborn
sns.set(style="whitegrid")

# Visualizing the distribution of Loan Amount
plt.figure(figsize=(10, 6))
sns.histplot(train_data['LoanAmount'], bins=30, kde=True)
plt.title('Distribution of Loan Amount')
plt.xlabel('Loan Amount')
plt.ylabel('Frequency')
plt.show()

# Visualizing the relationship between Applicant Income and Loan Amount
plt.figure(figsize=(10, 6))
sns.scatterplot(data=train_data, x='ApplicantIncome', y='LoanAmount', hue='Loan_Status')
plt.title('Applicant Income vs Loan Amount')
plt.xlabel('Applicant Income')
plt.ylabel('Loan Amount')
plt.legend(title='Loan Status', loc='upper right')
plt.show()

# Countplot for Education vs Loan Status
plt.figure(figsize=(10, 6))
sns.countplot(data=train_data, x='Education', hue='Loan_Status')
plt.title('Loan Status by Education Level')
plt.xlabel('Education')
plt.ylabel('Count')
plt.legend(title='Loan Status')
plt.show()

# Count the number of loans by property area
plt.figure(figsize=(10, 6))
sns.countplot(data=train_data, x='Property_Area', hue='Loan_Status')
plt.title('Loan Status by Property Area')
plt.xlabel('Property Area')
plt.ylabel('Count')
plt.legend(title='Loan Status')
plt.show()

# Visualizing the correlation matrix
plt.figure(figsize=(12, 8))

# Drop non-numeric columns before calculating the correlation
correlation = train_data.select_dtypes(include=['float64', 'int64']).corr()

sns.heatmap(correlation, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Matrix')
plt.show()