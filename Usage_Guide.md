# Usage Guide – Exploratory Data Analysis (EDA) Project
## Introduction
This guide explains how to set up, run, and understand the Exploratory Data Analysis (EDA) project. The project analyzes customer purchase data using Python and generates statistical summaries and visualizations.

## Prerequisites
Before running the project, make sure the following software is installed on your system:
Required Software
- Python 3.8 or above
- Jupyter Notebook (optional)
- VS Code / PyCharm / Any Python IDE

## Install Required Libraries
- Open terminal or command prompt and run:
- pip install -r requirements.txt
This installs:
- pandas
- numpy
- matplotlib
- seaborn
- scikit-learn
- jupyter

## Project Folder Setup
Create the following folder structure:
EDA_Project/
│
├── data/
├── notebooks/
├── src/
├── images/
├── requirements.txt
├── README.md
└── main.py

## Add Dataset
Place the dataset file inside the data/ folder.
Example:
- data/customer_data.csv

## Run the Project
Navigate to the project directory:
- cd EDA_Project

Run the main Python file:
- python main.py

## What Happens After Running
The project automatically performs:
- Data Loading
- Reads CSV dataset
- Displays first rows
- Data Cleaning
- Removes duplicates
- Handles missing values
- Statistical Analysis
- Mean
- Median
- Standard deviation
- Min/Max values
- Data Visualization

## The project generates:

- Histograms
- Bar charts
- Correlation heatmaps
- Boxplots

## All images are saved inside:
images/

## Start Jupyter Notebook:

jupyter notebook
Open:
notebooks/eda_analysis.ipynb
Run cells one by one to observe:

- Dataset loading
- Statistical analysis
- Graph generation
- Insights extraction