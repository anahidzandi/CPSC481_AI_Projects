from sklearn.neighbors import KNeighborsRegressor
import numpy as np

# define the dataset
X_train = np.array([[65.75], [71.52], [69.40], [68.22], [67.79], [68.70], [69.80], [70.01], [67.90], [66.49]])
y_train = np.array([112.99, 136.49, 153.03, 142.34, 144.30, 123.30, 141.49, 136.46, 112.37, 127.45])

# create the KNN object
knn = KNeighborsRegressor(n_neighbors=3)

# fit the model
knn.fit(X_train, y_train)

# predict the weight
X_test = np.array([[60], [63], [72], [65]])
y_pred = knn.predict(X_test)

# open the output file for writing
with open("output.txt", "w") as f:
    print("Predicted weights for the following heights:", file=f)
    for i in range(len(X_test)):
        print("Height:", X_test[i][0], "Predicted weight:", y_pred[i], file=f)

print("Output written to output.txt")
