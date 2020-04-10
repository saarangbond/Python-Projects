import pandas as pd

movies_df = pd.read_csv("IMDB-Movie-Data.csv", index_col = "Title")

'''
print(movies_df.head())
print(movies_df.tail(2))
print()
print(movies_df.info())
print()
print(movies_df.shape)
print()
'''

temp_df = movies_df.append(movies_df)
##print(temp_df.shape)
temp_df = temp_df.drop_duplicates()
##print(temp_df.shape)
####print()

##print(movies_df.columns)
movies_df.rename(columns = {
    'Runtime (Minutes)':'Runtime',
    'Revenue (Millions)':'Revenue'

}, inplace = True)

##print(movies_df.columns)

movies_df.columns = [col.lower() for col in movies_df]
##print(movies_df.columns)
##print()


## two options for removing nulls:
## deleting the rows (or columns) with nulls, or
## replacing the null values with non-null values (imputation)

print(movies_df.isnull().sum())
print()
##to drop rows with null values, use movies_df = movies_df.dropna()
##to drop columns with null values, use movies_df = movies_df.dropna(axis = 1)

# imputation
## imputation is usually done by imputing the null values with another value,
## usually the mean or median of that column

revenue = movies_df['revenue']
revenue_mean = revenue.mean()
revenue.fillna(revenue_mean, inplace=True)
print(revenue.head())
print()
print(movies_df.isnull().sum())
print()
print(movies_df['genre'].describe())
print()
print(movies_df['genre'].value_counts().head(10))
print()
print(movies_df.corr())