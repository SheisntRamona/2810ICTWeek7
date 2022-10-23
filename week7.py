import panads as pd

data = pd.read_csv(r'winereviews.csv')
df = pd.DataFrame(data)

#what countries are in the dataset?
print(df["Country"].unique())

#wines with a score of 100
print(df[df["Score"] == 100])

#wines with a cost over $1000
print(df[df["Cost"] > 1000])

#highest rated wine for each variety
df = pd.DataFrame(data)
df = df.sortvalues("Rating", ascending=False)
df = df.drop_duplicates(subset=['variety'], keep="first")

print(df)

#lowest rated wine for each variety
df = pd.DataFrame(data)
df = df.sortvalues("Rating", ascending=True)
df = df.drop_duplicates(subset=['variety'], keep="first")

print(df)

#wines with highest points-to-price ratio
df = pd.DataFrame(data)
print(df.groupby(['points', 'price'].head(10)))

#average price for each country and variety 
df = pd.DataFrame(data)
print(df.groupby(['variety'])['price'].mean())
print(df.groupby('country')['price'].mean())
print(df.groupby(['variety', 'country'])['price'].mean())

#average score for each country and variety
df = pd.DataFrame(data)
print(df.groupby('variety')['score'].mean())
print(df.groupby('country')['score'].mean())
print(df.groupby(['variety', 'country'])['score'].mean())
