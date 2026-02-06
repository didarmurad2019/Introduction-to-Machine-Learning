print("=== FEATURE ENGINEERING INSIGHTS ===")

# Create new engineered features
df['family_size'] = df['sibsp'] + df['parch'] + 1  # Total family members including passenger
df['is_child'] = (df['age'] < 12).astype(int)  # Binary flag for children
df['is_elderly'] = (df['age'] > 60).astype(int)  # Binary flag for elderly
df['fare_per_person'] = df['fare'] / df['family_size']  # Adjusted fare per person

# Create 2x2 grid for analyzing new features
fig, axes = plt.subplots(2, 2, figsize=(15, 10))

# 1. Family Size vs Survival
family_survival = df.groupby('family_size')['survived'].mean()
axes[0,0].plot(family_survival.index, family_survival.values, marker='o', linewidth=2)
axes[0,0].set_title('Survival Rate by Family Size', fontweight='bold')
axes[0,0].set_xlabel('Family Size')
axes[0,0].set_ylabel('Survival Rate')
axes[0,0].grid(True, alpha=0.3)

# 2. Fare per person analysis
df['fare_per_person_group'] = pd.qcut(df['fare_per_person'], q=4, 
                                      labels=['Q1', 'Q2', 'Q3', 'Q4'])
fare_survival = df.groupby('fare_per_person_group')['survived'].mean()
axes[0,1].bar(fare_survival.index.astype(str), fare_survival.values, color='#9b59b6')
axes[0,1].set_title('Survival Rate by Fare per Person Quartile', fontweight='bold')
axes[0,1].set_xlabel('Fare per Person Quartile')
axes[0,1].set_ylabel('Survival Rate')

# 3. Children vs Adults survival comparison
child_survival = df.groupby('is_child')['survived'].mean()
axes[1,0].bar(['Adult', 'Child'], child_survival.values, color=['#3498db', '#e74c3c'])
axes[1,0].set_title('Survival Rate: Children vs Adults', fontweight='bold')
axes[1,0].set_ylabel('Survival Rate')
for i, val in enumerate(child_survival.values):
    axes[1,0].text(i, val + 0.01, f'{val:.2%}', ha='center')

# 4. Title-based analysis
df['title'] = df['who'].str.capitalize()  # Extract and capitalize titles
title_survival = df.groupby('title')['survived'].mean().sort_values(ascending=False)
axes[1,1].bar(title_survival.index, title_survival.values, color=sns.color_palette("husl", 3))
axes[1,1].set_title('Survival Rate by Title', fontweight='bold')
axes[1,1].set_ylabel('Survival Rate')
for i, (idx, val) in enumerate(title_survival.items()):
    axes[1,1].text(i, val + 0.01, f'{val:.2%}', ha='center')

plt.tight_layout()
plt.show()