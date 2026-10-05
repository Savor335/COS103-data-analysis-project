import pandas as pd
import matplotlib.pyplot as plt


# 1. Load the dataset into a DataFrame
load = pd.read_csv(r"C:\Users\HP\Documents\pratice\Iris.csv")

print(load.head())
print(load.info())

# 2. Summary statistics
print("\n--- Summary statistics (all data) ---")
print(load.describe())

# 3. Check for missing values
print("\nMissing values per column:")
print(load.isnull().sum())

# 4. Visualizations


# Histogram of each feature
load.drop(columns="Species").hist(figsize=(9, 8), bins=19)
plt.suptitle("Distribution of Iris")
plt.tight_layout()
plt.savefig("iris_histograms.png")
plt.show()

# Boxplot: compare a feature across species
plt.figure(figsize=(8, 6))
load.boxplot(column="PetalLengthCm", by="Species")
plt.title("Petal Length by Species")
plt.savefig("iris_boxplot.png")
plt.show()

# Scatter plot: two features colored by species
plt.figure(figsize=(8, 6))
plt.scatter(load["PetalLengthCm"], load["PetalWidthCm"])
plt.xlabel("Petal Length (cm)")
plt.ylabel("Petal Width (cm)")
plt.title("Petal Length vs Petal Width")
plt.savefig("iris_scatter.png")
plt.show()


print("\nAll plots saved as PNG files in the current folder.")