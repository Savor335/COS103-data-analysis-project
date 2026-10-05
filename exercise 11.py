import pandas as pd
import matplotlib.pyplot as plt


# 1. Load the dataset into a DataFrame
df = pd.read_csv(r"C:\Users\HP\Documents\pratice\Iris.csv")

print(df.head())
print(df.info())

# 2. Summary statistics
print("\n--- Summary statistics (all data) ---")
print(df.describe())

print("\n--- Summary statistics by species ---")
print(df.groupby("Species").mean(numeric_only=True))

# 3. Check for missing values
print("\nMissing values per column:")
print(df.isnull().sum())

# 4. Visualizations


# Histogram of each feature
df.drop(columns="Species").hist(figsize=(10, 8), bins=20)
plt.suptitle("Distribution of Iris Features")
plt.tight_layout()
plt.savefig("iris_histograms.png")
plt.show()

# Boxplot: compare a feature across species
plt.figure(figsize=(8, 6))

plt.title("Petal Length by Species")
plt.savefig("iris_boxplot.png")
plt.show()

# Scatter plot: two features colored by species
plt.figure(figsize=(8, 6))

plt.title("Petal Length vs Petal Width")
plt.savefig("iris_scatter.png")
plt.show()

# Pairplot: every feature against every other, colored by species

plt.savefig("iris_pairplot.png")
plt.show()

# Correlation heatmap
plt.figure(figsize=(6, 5))

plt.title("Correlation Between Features")
plt.savefig("iris_correlation.png")
plt.show()

print("\nAll plots saved as PNG files in the current folder.")