import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Dataset load
df = pd.read_csv("books_data.csv")

# Price clean
df["Price"] = (
    df["Price"]
    .str.replace("£", "", regex=False)
    .str.replace("Â", "", regex=False)
    .astype(float)
)

# -------------------------------
# 1️⃣ Rating Distribution (Bar Chart)
# -------------------------------
plt.figure(figsize=(6,4))
sns.countplot(x="Rating", data=df)
plt.title("Book Rating Distribution")
plt.xlabel("Rating")
plt.ylabel("Number of Books")
plt.tight_layout()
plt.show()

# -------------------------------
# 2️⃣ Price Distribution (Histogram)
# -------------------------------
plt.figure(figsize=(6,4))
plt.hist(df["Price"], bins=20)
plt.title("Book Price Distribution")
plt.xlabel("Price (£)")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()

# -------------------------------
# 3️⃣ Availability Distribution (Pie Chart)
# -------------------------------
availability_counts = df["Availability"].value_counts()

plt.figure(figsize=(5,5))
plt.pie(
    availability_counts,
    labels=availability_counts.index,
    autopct="%1.1f%%",
    startangle=90
)
plt.title("Book Availability")
plt.tight_layout()
plt.show()
