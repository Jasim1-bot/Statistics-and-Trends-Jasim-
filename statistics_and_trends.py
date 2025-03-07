"""
This is the template file for the statistics and trends assignment.
You will be expected to complete all the sections and
make this a fully working, documented file.
You should NOT change any function, file or variable names,
if they are given to you here.
Make use of the functions presented in the lectures
and ensure your code is PEP-8 compliant, including docstrings.
"""

from corner import corner
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy.stats as ss
import seaborn as sns

def plot_relational_plot(df):
    """Generate and save a relational plot."""
    fig, ax = plt.subplots()
    plt.savefig('relational_plot.png')
    return

def plot_categorical_plot(df):
    """Generate and save a categorical plot."""
    fig, ax = plt.subplots()
    plt.savefig('categorical_plot.png')
    return

def plot_statistical_plot(df):
    """Generate and save a statistical plot."""
    fig, ax = plt.subplots()
    plt.savefig('statistical_plot.png')
    return

def statistical_analysis(df, col: str):
    """Perform statistical analysis on the specified column."""
    mean = df[col].mean()
    stddev = df[col].std()
    skew = ss.skew(df[col], nan_policy='omit')
    excess_kurtosis = ss.kurtosis(df[col], nan_policy='omit')
    return mean, stddev, skew, excess_kurtosis

def preprocessing(df):
    """Preprocess the dataset by handling missing values and analyzing correlations."""
    print(df.describe(include='all'))
    print(df.head())
    print(df.corr(numeric_only=True))
    return df.dropna()

def writing(moments, col):
    """Print statistical moments for the given column."""
    print(f'For the attribute {col}:')
    print(f'Mean = {moments[0]:.2f}, '
          f'Standard Deviation = {moments[1]:.2f}, '
          f'Skewness = {moments[2]:.2f}, and '
          f'Excess Kurtosis = {moments[3]:.2f}.')
    skew_desc = "Right-skewed" if moments[2] > 0 else "Left-skewed" if moments[2] < 0 else "Symmetrical"
    kurtosis_desc = "Leptokurtic" if moments[3] > 0 else "Platykurtic" if moments[3] < 0 else "Mesokurtic"
    print(f'The data is {skew_desc} and {kurtosis_desc}.')
    return

def scatter_plot(df, file_name):
    """Generate and save a scatter plot."""
    plt.figure(figsize=(8, 6))
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    if len(numeric_cols) < 2:
        print(f"Insufficient numerical columns in {file_name}.")
        return
    sns.scatterplot(data=df, x=numeric_cols[0], y=numeric_cols[1], color='blue', alpha=0.7, edgecolor='black')
    plt.xlabel(numeric_cols[0])
    plt.ylabel(numeric_cols[1])
    plt.title(f"Scatter Plot - {file_name}", fontsize=14)
    plt.grid(True)
    plt.savefig(f'scatter_{file_name}.png')
    plt.close()

def bar_plot(df, file_name):
    """Generate and save a bar chart."""
    plt.figure(figsize=(10, 6))
    category_cols = df.select_dtypes(include=['object', 'category']).columns
    if len(category_cols) == 0:
        print(f"No categorical data in {file_name}.")
        return
    sns.countplot(x=category_cols[0], data=df, palette='viridis')
    plt.xlabel(category_cols[0])
    plt.ylabel("Count")
    plt.title(f"Bar Chart - {file_name}", fontsize=14)
    plt.xticks(rotation=45)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.savefig(f'bar_{file_name}.png')
    plt.close()

def heatmap(df, file_name):
    """Generate and save a heatmap of correlations."""
    plt.figure(figsize=(8, 6))
    numeric_data = df.select_dtypes(include=[np.number])
    if numeric_data.shape[1] < 2:
        print(f"Not enough numeric data in {file_name}.")
        return
    sns.heatmap(numeric_data.corr(), annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
    plt.title(f"Heatmap - {file_name}", fontsize=14)
    plt.savefig(f'heatmap_{file_name}.png')
    plt.close()

def main():
    """Main function to execute data processing and visualization."""
    file_name = 'data.csv'
    try:
        df = pd.read_csv(file_name, encoding='utf-8', on_bad_lines='skip')
    except FileNotFoundError:
        print(f"File {file_name} not found.")
        return
    except pd.errors.ParserError:
        print(f"Error reading {file_name}, check formatting.")
        return
    
    df = preprocessing(df)
    num_cols = df.select_dtypes(include=[np.number]).columns
    if len(num_cols) == 0:
        print(f"No numeric data in {file_name}.")
        return
    
    selected_col = num_cols[0]
    plot_relational_plot(df)
    plot_statistical_plot(df)
    plot_categorical_plot(df)
    scatter_plot(df, file_name)
    heatmap(df, file_name)
    bar_plot(df, file_name)
    moments = statistical_analysis(df, selected_col)
    writing(moments, selected_col)
    
if __name__ == '__main__':import logging

# Create a logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Create a file handler
file_handler = logging.FileHandler('statistics_and_trends.log')
file_handler.setLevel(logging.INFO)

# Create a console handler
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

# Create a formatter and set it for the handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# Add the handlers to the logger
logger.addHandler(file_handler)
logger.addHandler(console_handler)

def plot_relational_plot(df):
    """Generate and save a relational plot."""
    try:
        fig, ax = plt.subplots()
        plt.savefig('relational_plot.png')
        logger.info('Relational plot saved successfully.')
    except Exception as e:
        logger.error(f'Failed to save relational plot: {str(e)}')
    return

def plot_categorical_plot(df):
    """Generate and save a categorical plot."""
    try:
        fig, ax = plt.subplots()
        plt.savefig('categorical_plot.png')
        logger.info('Categorical plot saved successfully.')
    except Exception as e:
        logger.error(f'Failed to save categorical plot: {str(e)}')
    return

def plot_statistical_plot(df):
    """Generate and save a statistical plot."""
    try:
        fig, ax = plt.subplots()
        plt.savefig('statistical_plot.png')
        logger.info('Statistical plot saved successfully.')
    except Exception as e:
        logger.error(f'Failed to save statistical plot: {str(e)}')
    return

def statistical_analysis(df, col: str):
    """Perform statistical analysis on the specified column."""
    try:
        mean = df[col].mean()
        stddev = df[col].std()
        skew = ss.skew(df[col], nan_policy='omit')
        excess_kurtosis = ss.kurtosis(df[col], nan_policy='omit')
        logger.info(f'Statistical analysis for column {col} completed successfully.')
        return mean, stddev, skew, excess_kurtosis
    except Exception as e:
        logger.error(f'Failed to perform statistical analysis for column {col}: {str(e)}')
        return None

def preprocessing(df):
    """Preprocess the dataset by handling missing values and analyzing correlations."""
    try:
        print(df.describe(include='all'))
        print(df.head())
        print(df.corr(numeric_only=True))
        logger.info('Data preprocessing completed successfully.')
        return df.dropna()
    except Exception as e:
        logger.error(f'Failed to preprocess data: {str(e)}')
        return None

def writing(moments, col):
    """Print statistical moments for the given column."""
    try:
        print(f'For the attribute {col}:')
        print(f'Mean = {moments[0]:.2f}, '
              f'Standard Deviation = {moments[1]:.2f}, '
              f'Skewness = {moments[2]:.2f}, and '
              f'Excess Kurtosis = {moments[3]:.2f}.')
        skew_desc = "Right-skewed" if moments[2] > 0 else "Left-skewed" if moments[2] < 0 else "Symmetrical"
        kurtosis_desc = "Leptokurtic" if moments[3] > 0 else "Platykurtic" if moments[3] < 0 else "Mesokurtic"
        print(f'The data is {skew_desc} and {kurtosis_desc}.')
        logger.info(f'Statistical moments for column {col} printed successfully.')
    except Exception as e:
        logger.error(f'Failed to print statistical moments for column {col}: {str(e)}')
    return

def scatter_plot(df, file_name):
    """Generate and save a scatter plot."""
    try:
        plt.figure(figsize=(8, 6))
        numeric_cols = df.select_dtypes(include=[np.number]).columns
        if len(numeric_cols) < 2:
            print(f"Insufficient numerical columns in {file_name}.")
            logger.warning(f'Insufficient numerical columns in {file_name}.')
            return
        sns.scatterplot(data=df, x=numeric_cols[0], y=numeric_cols[1], color='blue', alpha=0.7, edgecolor='black')
        plt.xlabel(numeric_cols[0])
        plt.ylabel(numeric_cols[1])
        plt.title(f"Scatter Plot - {file_name}", fontsize=14)
        plt.grid(True)
        plt.savefig(f'scatter_{file_name}.png')
        plt.close()
        logger.info(f'Scatter plot for {file_name} saved successfully.')
    except Exception as e:
        logger.error(f'Failed to save scatter plot for {file_name}: {str(e)}')
    return

def bar_plot(df, file_name):
    """Generate and save a bar chart."""
    try:
        plt.figure(figsize=(10, 6))
        category_cols = df.select_dtypes(include=['object', 'category']).columns
        if len(category_cols) == 0:
            print(f"No categorical data in {file_name}.")
            logger.warning(f'No categorical data in {file_name}.')
            return
        sns.countplot(x=category_cols[0], data=df, palette='viridis')
        plt.xlabel(category_cols[0])
        plt.ylabel("Count")
        plt.title(f"Bar Chart - {file_name}", fontsize=14)
        plt.xticks(rotation=45)
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        plt.savefig(f'bar_{file_name}.png')
        plt.close()
        logger.info(f'Bar chart for {file_name} saved successfully.')
    except Exception as e:
        logger.error(f'Failed to save bar chart for {file_name}: {str(e)}')
    return

def heatmap(df, file_name):
    """Generate and save a heatmap of correlations."""
    try:
        plt.figure(figsize=(8, 6))
        numeric_data = df.select_dtypes(include=[np.number])
        if numeric_data.shape[1] < 2:
            print(f"Not enough numeric data in {file_name}.")
            logger.warning(f'Not enough numeric data in {file_name}.')
            return
        sns.heatmap(numeric_data.corr(), annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
        plt.title(f"Heatmap - {file_name}", fontsize=14)
        plt.savefig(f'heatmap_{file_name}.png')
        plt.close()
        logger.info(f'Heatmap for {file_name} saved successfully.')
    except Exception as e:
        logger.error(f'Failed to save heatmap for {file_name}: {str(e)}')
    return

def main():
    """Main function to execute data processing and visualization."""
    file_name = 'data.csv'
    try:
        df = pd.read_csv(file_name, encoding='utf-8', on_bad_lines='skip')
        logger.info(f'Data loaded from {file_name} successfully.')
    except FileNotFoundError:
        print(f"File {file_name} not found.")
        logger.error(f'File {file_name} not found.')
        return
    except pd.errors.ParserError:
        print(f"Error reading {file_name}, check formatting.")
        logger.error(f'Error reading {file_name}, check formatting.')
        return
    
    df = preprocessing(df)
    num_cols = df.select_dtypes(include=[np.number]).columns
    if len(num_cols) == 0:
        print(f"No numeric data in {file_name}.")
        logger.warning(f'No numeric data in {file_name}.')
        return
    
    selected_col = num_cols[0]
    plot_relational_plot(df)
    plot_statistical_plot(df)
    plot_categorical_plot(df)
    scatter_plot(df, file_name)
    heatmap(df, file_name)
    bar_plot(df, file_name)
    moments = statistical_analysis(df, selected_col)
    writing(moments, selected_col)
    
if __name__ == '__main__':
    main()
    main()
