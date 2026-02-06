# Import essential data analysis and visualization libraries
import numpy as np  # Numerical computing for arrays and matrices
import pandas as pd  # Data manipulation and analysis with DataFrames
import matplotlib.pyplot as plt  # Core plotting library for static visualizations
import seaborn as sns  # Statistical data visualization built on matplotlib
import warnings  # Manage warning messages during execution

# Suppress warning messages for cleaner output during analysis
warnings.filterwarnings('ignore')

# Configure visualization aesthetics
sns.set_style("whitegrid")  # Apply Seaborn's whitegrid style for clean plots
plt.rcParams['figure.figsize'] = (10, 6)  # Set default figure size to 10x6 inches