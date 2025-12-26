import pandas as pd

# 1️⃣ Dataset load
df = pd.read_csv("books_data.csv")

print("First 5 rows:")
print(df.head())

# 2️⃣ Dataset info
print("\nDataset Info:")
print(df.info())

# 3️⃣ Price column clean
df["Price"] = (
    df["Price"]
    .str.replace("£", "", regex=False)
    .str.replace("Â", "", regex=False)
    .astype(float)
)


# 4️⃣ Basic statistics
print("\nStatistical Summary:")
print(df.describe())

# 5️⃣ Key insights
print("\nAverage Price:", round(df["Price"].mean(), 2))
print("Highest Price:", df["Price"].max())
print("Lowest Price:", df["Price"].min())

print("\nRating Distribution:")
print(df["Rating"].value_counts())

print("\nAvailability Count:")
print(df["Availability"].value_counts())
