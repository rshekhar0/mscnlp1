import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
from sklearn.datasets import load_iris

class NaiveBayesClassifier:
    def __init__(self):
        self.means = None
        self.variances = None
        self.priors = None
        self.classes = None
    
    def fit(self, X, y):
        self.classes = np.unique(y)
        self.means = np.zeros((len(self.classes), X.shape[1]))
        self.variances = np.zeros((len(self.classes), X.shape[1]))
        self.priors = np.zeros(len(self.classes))
        
        for i, c in enumerate(self.classes):
            X_c = X[y == c]
            self.means[i, :] = X_c.mean(axis=0)
            self.variances[i, :] = X_c.var(axis=0)
            self.priors[i] = X_c.shape[0] / float(X.shape[0])
    
    def predict(self, X):
        likelihoods = self._calculate_likelihood(X)
        posteriors = self._calculate_posterior(likelihoods)
        return self.classes[np.argmax(posteriors, axis=1)]
    
    def _calculate_likelihood(self, X):
        likelihoods = np.zeros((X.shape[0], len(self.classes)))
        for i, c in enumerate(self.classes):
            mean = self.means[i]
            variance = self.variances[i]
            likelihood = (1 / np.sqrt(2 * np.pi * variance)) * np.exp(-(X - mean) ** 2 / (2 * variance))
            likelihoods[:, i] = np.prod(likelihood, axis=1)
        return likelihoods
    
    def _calculate_posterior(self, likelihoods):
        posteriors = likelihoods * self.priors
        return posteriors

# Example usage with the Iris dataset
def main():
    # Load dataset
    iris = load_iris()
    X = iris.data
    y = iris.target
    
    # Split dataset
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    
    # Initialize and train classifier
    model = NaiveBayesClassifier()
    model.fit(X_train, y_train)
    
    # Make predictions
    y_pred = model.predict(X_test)
    
    # Calculate accuracy
    accuracy = accuracy_score(y_test, y_pred)
    print(f'Accuracy: {accuracy * 100:.2f}%')
    
    # Print classification report
    report = classification_report(y_test, y_pred, target_names=iris.target_names)
    print('Classification Report:')
    print(report)

if __name__ == "__main__":
    main()
