from sklearn.model_selection import KFold
import numpy as np

def perform_cross_validation(model, x, y):
    models = []
    accuracies = []
    splitter = KFold(n_splits=10)
    
    for train_indices, test_indices in splitter.split(x, y):
        X_train, y_train = x.iloc[train_indices], y.iloc[train_indices]
        X_test, y_test = x.iloc[test_indices], y.iloc[test_indices]

        trained_model = model.fit(X_train, y_train)
        predictions = trained_model.predict(X_test)
        accuracy = calculate_accuracy(predictions, y_test)
        accuracies.append(accuracy)
        models.append(trained_model)

    print("Average Validation Score: %.2f" %np.mean(accuracies))

    best_model = models[identify_best_model(accuracies)]
    return best_model
    
# Caluclates the accuracy of a model given the predicted and real values
def calculate_accuracy(pred, real):
    return len(np.where(pred == real)[0]) / len(pred)

def identify_best_model(accuracies):
    best_score = max(accuracies)
    return accuracies.index(best_score) 