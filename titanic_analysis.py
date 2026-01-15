#!/usr/bin/env python3
"""
Titanic Dataset Analysis Script
Basic exploration of the Titanic dataset
"""

import pandas as pd
import numpy as np

print("Loading dataset...")
df = pd.read_csv("titanic_data/train.csv")
print("Dataset loaded\n")

print("First 5 rows:")
print(df.head())

print("\nLast 5 rows:")
print(df.tail())

print("\nDataset shape:")
print(df.shape)

print("\nColumn names:")
print(df.columns.tolist())

print("\nData types and missing values:")
df.info()

print("\nStatistical summary:")
print(df.describe())

survival_rate = df["Survived"].mean() * 100
print(f"\nSurvival rate: {survival_rate:.2f}%")

print("\nCategorical distributions:")

print("\nSex:")
print(df["Sex"].value_counts())

print("\nPassenger Class:")
print(df["Pclass"].value_counts().sort_index())

print("\nEmbarked:")
print(df["Embarked"].value_counts())

print("\nMissing values analysis:")
missing = df.isnull().sum()
missing_percent = (missing / len(df)) * 100

issues = pd.DataFrame({
    "Missing": missing,
    "Percent": missing_percent
})
issues = issues[issues["Missing"] > 0]
print(issues.sort_values("Percent", ascending=False))

print("\nSummary:")
print("Target variable: Survived")
print("Main issues: Missing Age and Cabin values")
print("Dataset is suitable for ML after preprocessing")
