print("=== CORRELATION ANALYSIS ===")

# Select numerical features for correlation analysis
num_features = ['survived', 'pclass', 'age', 'sibsp', 'parch', 'fare', 'has_deck']
corr_matrix = df[num_features].corr()

# Create correlation heatmap
plt.figure(figsize=(12, 8))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', center=0, 
            square=True, linewidths=1, cbar_kws={"shrink": 0.8})
plt.title('Correlation Matrix of Numerical Features', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.show()

# Extract and display top correlations with survival
print("\nTop Features Correlated with Survival:")
survival_corr = corr_matrix['survived'].sort_values(ascending=False)
for feature, corr in survival_corr.items():
    if feature != 'survived':  # Skip correlation with itself
        print(f"  {feature}: {corr:.3f}")