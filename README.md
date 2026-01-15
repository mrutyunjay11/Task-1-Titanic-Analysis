# Titanic Dataset Analysis – Task 1

## Task Objective
The objective of this task is to understand the structure of a dataset,
identify different data types, analyze data quality issues, and check
whether the dataset is suitable for machine learning.

This task focuses on exploratory data analysis before applying any ML models.

---

## Dataset Used
**Titanic Dataset (train.csv)**  
Source: Kaggle – Titanic: Machine Learning from Disaster

The dataset contains information about 891 passengers, including:
- Personal details (age, sex, name)
- Travel details (class, fare, embarkation port)
- Survival status

---

## Tools and Technologies
- Python 3
- Pandas
- NumPy
- Jupyter Notebook
- VS Code / Terminal
- Git & GitHub

---

## Steps Performed

1. Loaded the dataset using Pandas.
2. Displayed first and last few records to understand the structure.
3. Checked dataset shape and column names.
4. Used `df.info()` to inspect data types and missing values.
5. Used `df.describe()` to analyze statistical properties.
6. Classified features into:
   - Numerical
   - Categorical
   - Ordinal
   - Binary
7. Analyzed categorical value distributions.
8. Identified the target variable (`Survived`) and input features.
9. Checked dataset size and suitability for machine learning.
10. Identified data quality issues such as missing values and imbalance.

---

## Feature Overview

- **Target Variable:** `Survived`
- **Numerical Features:** Age, Fare
- **Categorical Features:** Sex, Embarked
- **Ordinal Feature:** Pclass
- **Binary Feature:** Survived

---

## Data Quality Observations

- `Cabin` column has more than 70% missing values.
- `Age` column has around 20% missing values.
- Some columns like `Name` and `Ticket` are not useful for modeling.
- The target variable shows class imbalance.

---

## Machine Learning Readiness

The dataset is suitable for machine learning classification tasks.
However, preprocessing steps such as handling missing values and
encoding categorical variables are required before modeling.

---

## Files in This Repository

- `task1_titanic_analysis.ipynb` – Main Jupyter Notebook analysis
- `titanic_analysis.py` – Python script version of analysis
- `dataset_analysis.md` – One-page dataset analysis report
- `titanic_data/train.csv` – Dataset file
- `.gitignore` – Files ignored by Git

---

## Final Outcome
This task helped in understanding the importance of data exploration
and data quality analysis before building machine learning models.

---
