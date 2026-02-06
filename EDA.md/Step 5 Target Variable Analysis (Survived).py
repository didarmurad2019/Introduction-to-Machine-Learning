print("=== TARGET VARIABLE: SURVIVED ===")

# Create 3 subplots to analyze survival from different perspectives
fig, axes = plt.subplots(1, 3, figsize=(18, 5))

# 1. Count plot of survival
survival_counts = df['survived'].value_counts()
bars1 = axes[0].bar(['Not Survived (0)', 'Survived (1)'], survival_counts.values, 
                    color=['#e74c3c', '#2ecc71'])
axes[0].set_title('Survival Count', fontsize=14, fontweight='bold')
axes[0].set_ylabel('Count')
# Add count and percentage on bars
for bar, count in zip(bars1, survival_counts.values):
    height = bar.get_height()
    axes[0].text(bar.get_x() + bar.get_width()/2., height + 10,
                f'{count}\n({count/len(df)*100:.1f}%)', 
                ha='center', va='bottom', fontweight='bold')

# 2. Pie chart for survival distribution
axes[1].pie(survival_counts.values, labels=['Not Survived', 'Survived'],
            autopct='%1.1f%%', colors=['#e74c3c', '#2ecc71'],
            explode=[0.05, 0], startangle=90)
axes[1].set_title('Survival Distribution', fontsize=14, fontweight='bold')

# 3. Survival rate by gender (one of the most important insights)
survival_by_sex = pd.crosstab(df['sex'], df['survived'], normalize='index') * 100
bars2 = axes[2].bar(survival_by_sex.index, survival_by_sex[1], color='#3498db')
axes[2].set_title('Survival Rate by Gender', fontsize=14, fontweight='bold')
axes[2].set_ylabel('Survival Rate (%)')
axes[2].set_ylim([0, 100])
# Add percentage values on bars
for bar, rate in zip(bars2, survival_by_sex[1]):
    height = bar.get_height()
    axes[2].text(bar.get_x() + bar.get_width()/2., height + 2,
                f'{rate:.1f}%', ha='center', va='bottom', fontweight='bold')

plt.tight_layout()
plt.show()

# Print summary statistics
print(f"\nOverall Survival Rate: {df['survived'].mean()*100:.1f}%")
print(f"\nSurvival by Gender:")
print(survival_by_sex)