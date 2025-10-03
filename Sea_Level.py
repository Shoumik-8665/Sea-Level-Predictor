import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')
    
    # Create scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], alpha=0.7, label='Original Data')
    
    # Get slope and y-intercept for first line of best fit (all data)
    slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    
    # Create array of years from 1880 to 2050 for prediction
    years_extended = np.arange(1880, 2051)
    
    # Calculate sea level predictions for first line
    sea_levels_predicted = slope * years_extended + intercept
    
    # Plot first line of best fit
    plt.plot(years_extended, sea_levels_predicted, 'r-', label='Best Fit Line (1880-2013)')
    
    # Get data from year 2000 onwards for second line
    df_recent = df[df['Year'] >= 2000]
    
    # Get slope and y-intercept for second line of best fit (recent data)
    slope_recent, intercept_recent, r_value_recent, p_value_recent, std_err_recent = linregress(
        df_recent['Year'], df_recent['CSIRO Adjusted Sea Level']
    )
    
    # Create array of years from 2000 to 2050 for recent prediction
    years_recent_extended = np.arange(2000, 2051)
    
    # Calculate sea level predictions for second line
    sea_levels_recent_predicted = slope_recent * years_recent_extended + intercept_recent
    
    # Plot second line of best fit
    plt.plot(years_recent_extended, sea_levels_recent_predicted, 'g-', label='Best Fit Line (2000-2013)')
    
    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    # Save plot and return data for testing
    plt.savefig('sea_level_plot.png')
    return plt.gca()

# For development testing
if __name__ == '__main__':
    draw_plot()
    plt.show()