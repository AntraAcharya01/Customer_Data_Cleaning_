import pandas as pd

df=pd.read_csv('C:/PythonProgramming/venv/Pandas_Program/Project/customer_shopping_behavior.csv')
print(df)

# removing nulls
df['Review Rating']=df.groupby('Category')['Review Rating'].transform(lambda x:x.fillna(x.median))

# proper naming for columns

df.columns=df.columns.str.lower()
df.columns=df.columns.str.replace(' ','_')
df=df.rename(columns={'purchase_amount_(usd)':'purchase_amount'})

#create column age group

labels=['young adult','adult','middle aged','senior']
df['age group']=pd.qcut(df['age'],q=4,labels=labels)

# Create column purchase days freuency

frequency_mapping={
    'Fortnightly': 14,
    'Weekly':7,
    'Monthly':30,
    'Quarterly':90,
    'Annual':365,
    'Every 3 month': 90
}

df['purchase_frequncy_days']=df['frequency_of_purchases'].map(frequency_mapping)
print(df.isnull().sum())
 
