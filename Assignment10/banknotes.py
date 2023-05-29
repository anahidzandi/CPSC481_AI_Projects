import csv
import random
from sklearn import svm
from sklearn.neighbors import KNeighborsClassifier

models = [svm.SVC(), KNeighborsClassifier(n_neighbors=1)]

# Read data
with open("banknotes.csv") as f:
    reader = csv.reader(f)
    next(reader)
    data = []
    for row in reader:
        data.append({
            "feature": [float(cell) for cell in row[:4]],
            "label": "Authentic" if row[4] == "0" else "Counterfeit"
        })

# Separate data
holdout = int(0.40 * len(data))
random.shuffle(data)
testing = data[:holdout]
training = data[holdout:]

# Evaluate based on different models
for model in models:
    # Train model
    X_training = [row["feature"] for row in training]
    y_training = [row["label"] for row in training]
    model.fit(X_training, y_training)

    # Make predictions
    X_testing = [row["feature"] for row in testing]
    y_testing = [row["label"] for row in testing]
    predictions = model.predict(X_testing)

    # Compute performance
    correct = (y_testing == predictions).sum()
    incorrect = (y_testing != predictions).sum()
    total = len(predictions)

    # Results
    print(f"Results for model {type(model).__name__}")
    print(f"Correct: {correct}")
    print(f"Incorrect: {incorrect}")
    print(f"Accuracy: {100 * correct / total:.2f}%\n")
