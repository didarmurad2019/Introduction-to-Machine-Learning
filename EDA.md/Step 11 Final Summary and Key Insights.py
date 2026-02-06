print("="*60)
print("TITANIC EDA - KEY INSIGHTS SUMMARY")
print("="*60)

# 1. Overall dataset statistics
print(f"\n1. DATASET OVERVIEW:")
print(f"   Total passengers: {len(df)}")
print(f"   Survival rate: {df['survived'].mean()*100:.1f}%")
print(f"   Features analyzed: {len(df.columns)}")

# 2. Key survival factors
print(f"\n2. KEY SURVIVAL FACTORS:")
print(f"   Gender: Female ({df[df['sex']=='female']['survived'].mean()*100:.1f}%) vs "
      f"Male ({df[df['sex']=='male']['survived'].mean()*100:.1f}%)")
print(f"   Passenger Class: 1st ({df[df['pclass']==1]['survived'].mean()*100:.1f}%) vs "
      f"2nd ({df[df['pclass']==2]['survived'].mean()*100:.1f}%) vs "
      f"3rd ({df[df['pclass']==3]['survived'].mean()*100:.1f}%)")
print(f"   Embarkation: Cherbourg ({df[df['embark_town']=='Cherbourg']['survived'].mean()*100:.1f}%) vs "
      f"Southampton ({df[df['embark_town']=='Southampton']['survived'].mean()*100:.1f}%)")

# 3. Demographic insights
print(f"\n3. DEMOGRAPHICS:")
print(f"   Average age: {df['age'].mean():.1f} years")
print(f"   Children (<12): {df['is_child'].sum()} ({df['is_child'].mean()*100:.1f}%)")
print(f"   Traveling alone: {df['alone'].sum()} ({df['alone'].mean()*100:.1f}%)")

# 4. Correlation insights
print(f"\n4. FEATURES STRONGLY CORRELATED WITH SURVIVAL:")
corr_with_survival = df.select_dtypes(include=[np.number]).corr()['survived'].sort_values(ascending=False)
top_features = corr_with_survival[1:4]  # Top 3 excluding survival itself
for feature, corr in top_features.items():
    direction = "positively" if corr > 0 else "negatively"
    print(f"   {feature}: {direction} correlated (r = {corr:.3f})")

# 5. Machine learning recommendations
print(f"\n5. RECOMMENDATIONS FOR ML MODELING:")
print(f"   - Use pclass, sex, age, fare as key features")
print(f"   - Consider creating interaction terms (e.g., gender × class)")
print(f"   - Handle outliers in fare")
print(f"   - Encode categorical variables (sex, embarked)")
print(f"   - Consider family-based features")

# 6. Save cleaned dataset
df.to_csv('titanic_cleaned.csv', index=False)
print(f"\n6. OUTPUT:")
print(f"   Cleaned dataset saved as 'titanic_cleaned.csv'")
print(f"   Original shape: {sns.load_dataset('titanic').shape}")
print(f"   Cleaned shape: {df.shape}")