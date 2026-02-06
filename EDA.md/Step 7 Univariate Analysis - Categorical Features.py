print("=== CATEGORICAL FEATURES ANALYSIS ===")

# Select categorical columns for analysis
cat_cols = ['pclass', 'sex', 'embarked', 'who', 'alone']

# Create 2x3 grid for categorical plots
fig, axes = plt.subplots(2, 3, figsize=(18, 10))
axes = axes.ravel()  # Flatten for easy iteration

for idx, col in enumerate(cat_cols):
    value_counts = df[col].value_counts()
    bars = axes[idx].bar(value_counts.index.astype(str), value_counts.values, 
                        color=sns.color_palette("Set2"))
    axes[idx].set_title(f'Distribution of {col.upper()}', fontweight='bold')
    axes[idx].set_xlabel(col)
    axes[idx].tick_params(axis='x', rotation=45)  # Rotate x-labels for readability
    
    # Add percentage labels on bars
    total = len(df)
    for bar, count in zip(bars, value_counts.values):
        height = bar.get_height()
        percent = (count/total)*100
        axes[idx].text(bar.get_x() + bar.get_width()/2., height + 5,
                      f'{percent:.1f}%', ha='center', va='bottom', fontsize=9)
    
    # Print categorical distribution
    print(f"\n{col.upper()}:")
    for val, count in value_counts.items():
        print(f"  {val}: {count} ({count/len(df)*100:.1f}%)")

# Hide the last subplot if not needed
if len(cat_cols) < 6:
    axes[-1].axis('off')

plt.tight_layout()
plt.show()