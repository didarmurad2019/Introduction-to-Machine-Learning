# Step 1: Import Libraries and Load Data
# Import essential data science libraries
import numpy as np  # Numerical operations
import pandas as pd  # Data manipulation and analysis
import matplotlib.pyplot as plt  # Basic plotting
import seaborn as sns  # Statistical visualization
import warnings  # To suppress warnings
warnings.filterwarnings('ignore')  # Ignore warning messages for cleaner output

# Set visual styles for better looking plots
sns.set_style("whitegrid")  # Use white grid background
plt.rcParams['figure.figsize'] = (10, 6)  # Set default figure size
%matplotlib inline  # Display plots inline in Jupyter notebook

# Load Titanic dataset directly from seaborn (built-in dataset)
df = sns.load_dataset('titanic')

# Alternative: Load from CSV if you have it locally
# df = pd.read_csv('titanic.csv')

print("Dataset loaded successfully!")
print(f"Shape: {df.shape}")  # Show number of rows and columns
print(f"\nColumns: {list(df.columns)}")  # List all column names
