def titanic_quick_eda(df):
    """Quick EDA function for Titanic dataset"""
    
    print("🚢 TITANIC QUICK EDA")
    print("="*50)
    
    # Survival rate calculation
    survival_rate = df['survived'].mean() * 100
    print(f"\n📊 Overall Survival Rate: {survival_rate:.1f}%")
    
    # Key factors analysis
    print("\n🔑 Key Survival Factors:")
    for col in ['sex', 'pclass', 'embarked']:
        if col in df.columns:
            survival_by = df.groupby(col)['survived'].mean() * 100
            print(f"\n{col.upper()}:")
            for val, rate in survival_by.items():
                print(f"  {val}: {rate:.1f}%")
    
    # Missing values summary
    print(f"\n⚠️  Missing Values: {df.isnull().sum().sum()}")
    missing_cols = df.columns[df.isnull().any()].tolist()
    if missing_cols:
        print(f"   Columns with missing values: {missing_cols}")
    
    # Return summary dictionary
    return {
        'survival_rate': survival_rate,
        'total_passengers': len(df),
        'features': list(df.columns),
        'missing_values': df.isnull().sum().sum()
    }

# Run quick analysis
results = titanic_quick_eda(df)