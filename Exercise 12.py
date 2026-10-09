
import pandas as pd

# 1. Load the dataset
iris_data = pd.read_csv(
    r"C:\Users\HP\Documents\pratice\Iris.csv"
)

# Remove the ID column because it is not useful for classification
iris_data = iris_data.drop(columns=["Id"])

# 2. Separate the features and target
features = [
    "SepalLengthCm",
    "SepalWidthCm",
    "PetalLengthCm",
    "PetalWidthCm"
]

target = "Species"


# 3. Calculate Gini impurity
def gini_impurity(data):
    total = len(data)

    if total == 0:
        return 0

    probabilities = data[target].value_counts() / total

    return 1 - sum(probabilities ** 2)


# 4. Find the best split
def find_best_split(data):
    best_gini = float("inf")
    best_feature = None
    best_value = None

    for feature in features:

        possible_values = sorted(data[feature].unique())

        for value in possible_values:

            left_side = data[data[feature] <= value]
            right_side = data[data[feature] > value]

            if len(left_side) == 0 or len(right_side) == 0:
                continue

            total = len(data)

            weighted_gini = (
                (len(left_side) / total) * gini_impurity(left_side)
                + (len(right_side) / total) * gini_impurity(right_side)
            )

            if weighted_gini < best_gini:
                best_gini = weighted_gini
                best_feature = feature
                best_value = value

    return best_feature, best_value


# 5. Create the decision tree
def build_tree(data, depth=0, max_depth=3):

    # If all rows belong to the same species
    if len(data[target].unique()) == 1:
        return data[target].iloc[0]

    # Stop when maximum depth is reached
    if depth >= max_depth:
        return data[target].mode()[0]

    feature, value = find_best_split(data)

    # If no useful split is found
    if feature is None:
        return data[target].mode()[0]

    left_data = data[data[feature] <= value]
    right_data = data[data[feature] > value]

    return {
        "feature": feature,
        "value": value,
        "left": build_tree(left_data, depth + 1, max_depth),
        "right": build_tree(right_data, depth + 1, max_depth)
    }


# 6. Make a prediction for one flower
def predict_one(row, tree):

    if not isinstance(tree, dict):
        return tree

    if row[tree["feature"]] <= tree["value"]:
        return predict_one(row, tree["left"])

    return predict_one(row, tree["right"])


# 7. Split the dataset manually
train_data = iris_data.sample(frac=0.8, random_state=42)

test_data = iris_data.drop(train_data.index)


# 8. Build the tree using the training data
decision_tree = build_tree(train_data)


# 9. Predict the test data
predictions = []

for _, flower in test_data.iterrows():
    predictions.append(
        predict_one(flower, decision_tree)
    )


# 10. Get the actual answers
actual_values = test_data[target].tolist()


# 11. Calculate accuracy
correct = 0

for actual, predicted in zip(actual_values, predictions):

    if actual == predicted:
        correct += 1

accuracy = correct / len(actual_values)


# 12. Calculate precision and recall for each species
species_names = iris_data[target].unique()

print("Accuracy:", round(accuracy, 2))

for species in species_names:

    true_positive = 0
    false_positive = 0
    false_negative = 0

    for actual, predicted in zip(actual_values, predictions):

        if actual == species and predicted == species:
            true_positive += 1

        elif actual != species and predicted == species:
            false_positive += 1

        elif actual == species and predicted != species:
            false_negative += 1

    if true_positive + false_positive != 0:
        precision = true_positive / (
            true_positive + false_positive
        )
    else:
        precision = 0

    if true_positive + false_negative != 0:
        recall = true_positive / (
            true_positive + false_negative
        )
    else:
        recall = 0

    print("\nSpecies:", species)
    print("Precision:", round(precision, 2))
    print("Recall:", round(recall, 2))
