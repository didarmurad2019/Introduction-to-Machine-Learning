print("=== NUMERICAL FEATURES ANALYSIS ===")

# Select numerical columns for analysis
num_cols = ['age', 'fare', 'sibsp', 'parch']

# Create 2x2 grid for histograms
fig, axes = plt.subplots(2, 2, figsize=(15, 10))
axes = axes.ravel()  # Flatten axes array for easy iteration

# Analyze each numerical column
for idx, col in enumerate(num_cols):
    # Histogram with Kernel Density Estimate (KDE)
    sns.histplot(data=df, x=col, kde=True, ax=axes[idx], color='#3498db')
    # Add mean and median lines
    axes[idx].axvline(df[col].mean(), color='red', linestyle='--', 
                      label=f'Mean: {df[col].mean():.1f}')
    axes[idx].axvline(df[col].median(), color='green', linestyle='--', 
                      label=f'Median: {df[col].median():.1f}')
    axes[idx].set_title(f'Distribution of {col.upper()}', fontweight='bold')
    axes[idx].set_xlabel(col)
    axes[idx].legend()
    
    # Print detailed statistics for each column
    print(f"\n{col.upper()}:")
    print(f"  Min: {df[col].min():.2f}")
    print(f"  Max: {df[col].max():.2f}")
    print(f"  Mean: {df[col].mean():.2f}")
    print(f"  Median: {df[col].median():.2f}")
    print(f"  Std: {df[col].std():.2f}")
    print(f"  Skewness: {df[col].skew():.2f}")  # Measure of distribution asymmetry

plt.tight_layout()
plt.show()

# Box plots for outlier detection
fig, axes = plt.subplots(2, 2, figsize=(15, 8))
axes = axes.ravel()

for idx, col in enumerate(num_cols):
    sns.boxplot(data=df, y=col, ax=axes[idx], color='#f39c12')
    axes[idx].set_title(f'Box Plot of {col.upper()}', fontweight='bold')
    axes[idx].set_ylabel(col)
    
    # Detect outliers using Interquartile Range (IQR) method
    Q1 = df[col].quantile(0.25)  # First quartile (25th percentile)
    Q3 = df[col].quantile(0.75)  # Third quartile (75th percentile)
    IQR = Q3 - Q1  # Interquartile range
    lower_bound = Q1 - 1.5 * IQR  # Lower bound for outliers
    upper_bound = Q3 + 1.5 * IQR  # Upper bound for outliers
    outliers = df[(df[col] < lower_bound) | (df[col] > upper_bound)]
    print(f"\n{col} outliers: {len(outliers)} ({len(outliers)/len(df)*100:.1f}%)")

plt.tight_layout()
plt.show()