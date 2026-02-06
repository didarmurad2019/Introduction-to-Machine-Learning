print("=== RELATIONSHIP WITH SURVIVAL ===")

# Create 2x3 grid for various survival analyses
fig, axes = plt.subplots(2, 3, figsize=(18, 12))

# 1. Survival by Passenger Class
sns.barplot(data=df, x='pclass', y='survived', ax=axes[0,0], 
            palette='coolwarm', errorbar=None)
axes[0,0].set_title('Survival Rate by Passenger Class', fontweight='bold')
axes[0,0].set_ylabel('Survival Rate')
axes[0,0].set_xlabel('Passenger Class')
# Add percentage labels on bars
for i, p in enumerate(axes[0,0].patches):
    axes[0,0].text(p.get_x() + p.get_width()/2., p.get_height() + 0.01,
                  f'{p.get_height():.2%}', ha='center')

# 2. Survival by Gender
sns.barplot(data=df, x='sex', y='survived', ax=axes[0,1], 
            palette='viridis', errorbar=None)
axes[0,1].set_title('Survival Rate by Gender', fontweight='bold')
axes[0,1].set_ylabel('Survival Rate')
for i, p in enumerate(axes[0,1].patches):
    axes[0,1].text(p.get_x() + p.get_width()/2., p.get_height() + 0.01,
                  f'{p.get_height():.2%}', ha='center')

# 3. Survival by Embarkation Port
sns.barplot(data=df, x='embark_town', y='survived', ax=axes[0,2], 
            palette='magma', errorbar=None, order=['Cherbourg', 'Queenstown', 'Southampton'])
axes[0,2].set_title('Survival Rate by Embarkation Port', fontweight='bold')
axes[0,2].set_ylabel('Survival Rate')
axes[0,2].set_xlabel('Port of Embarkation')
for i, p in enumerate(axes[0,2].patches):
    axes[0,2].text(p.get_x() + p.get_width()/2., p.get_height() + 0.01,
                  f'{p.get_height():.2%}', ha='center')

# 4. Create age groups and analyze survival
df['age_group'] = pd.cut(df['age'], bins=[0, 12, 18, 35, 50, 80], 
                         labels=['Child', 'Teen', 'Young Adult', 'Adult', 'Senior'])
survival_by_age = df.groupby('age_group')['survived'].mean().sort_index()
axes[1,0].bar(survival_by_age.index.astype(str), survival_by_age.values, color='#e67e22')
axes[1,0].set_title('Survival Rate by Age Group', fontweight='bold')
axes[1,0].set_ylabel('Survival Rate')
axes[1,0].set_xlabel('Age Group')
for i, (idx, val) in enumerate(survival_by_age.items()):
    axes[1,0].text(i, val + 0.01, f'{val:.2%}', ha='center')

# 5. Survival by Traveling Alone
sns.barplot(data=df, x='alone', y='survived', ax=axes[1,1], 
            palette='Set2', errorbar=None)
axes[1,1].set_title('Survival Rate: Traveling Alone', fontweight='bold')
axes[1,1].set_ylabel('Survival Rate')
axes[1,1].set_xlabel('Alone (True=Alone)')
axes[1,1].set_xticklabels(['Not Alone', 'Alone'])
for i, p in enumerate(axes[1,1].patches):
    axes[1,1].text(p.get_x() + p.get_width()/2., p.get_height() + 0.01,
                  f'{p.get_height():.2%}', ha='center')

# 6. Fare distribution by survival (using box plots)
df['fare_group'] = pd.qcut(df['fare'], q=4, labels=['Low', 'Medium-Low', 'Medium-High', 'High'])
sns.boxplot(data=df, x='fare_group', y='fare', hue='survived', ax=axes[1,2], palette='coolwarm')
axes[1,2].set_title('Fare Distribution by Survival', fontweight='bold')
axes[1,2].set_xlabel('Fare Quartile Group')
axes[1,2].set_ylabel('Fare')
axes[1,2].legend(title='Survived', labels=['No', 'Yes'])

plt.tight_layout()
plt.show()