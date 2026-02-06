print("=== MISSING VALUE ANALYSIS ===")

# Create heatmap to visualize missing values pattern
plt.figure(figsize=(12, 6))
sns.heatmap(df.isnull(), yticklabels=False, cbar=False, cmap='viridis', 
            xticklabels=df.columns, cmap='RdYlGn_r')
plt.title('Missing Values Heatmap (Red = Missing)', fontsize=14, pad=20)
plt.tight_layout()
plt.show()

# Calculate missing value percentage for each column
missing_percent = (df.isnull().sum() / len(df)) * 100
missing_df = pd.DataFrame({
    'column': df.columns,
    'missing_count': df.isnull().sum(),
    'missing_percent': missing_percent
}).sort_values('missing_percent', ascending=False)

print("\nMissing Values Summary:")
print(missing_df[missing_df['missing_count'] > 0])

# Handle missing values using different strategies
print("\nHandling missing values...")

# Age: Fill missing values with median based on passenger class and gender
df['age'] = df.groupby(['pclass', 'sex'])['age'].transform(
    lambda x: x.fillna(x.median()))

# Embarked: Only 2 missing values, fill with most frequent value (mode)
df['embarked'] = df['embarked'].fillna(df['embarked'].mode()[0])
df['embark_town'] = df['embark_town'].fillna(df['embark_town'].mode()[0])

# Deck: Too many missing values (77%), create binary flag instead of dropping
df['has_deck'] = df['deck'].notnull().astype(int)  # 1 if deck info exists, 0 otherwise
df = df.drop('deck', axis=1)  # Drop original deck column due to high missing rate

print(f"Missing values after treatment: {df.isnull().sum().sum()}")