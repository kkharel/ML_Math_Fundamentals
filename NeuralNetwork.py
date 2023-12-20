# Create a single neuron to  be used in neural network,


import numpy as np

# Set a random seed for reproducibility
np.random.seed(7)

# Generate a small synthetic binary classification dataset
X = np.random.rand(100000, 3)  # 20 examples with 2 features each
y = np.random.randint(2, size=100000)  # Binary labels (0 or 1)

# Create a list of examples in the format expected by the Neuron class
dataset = [{"features": features.tolist(), "label": label} for features, label in zip(X, y)]

for example in dataset[:4]:
  print(f"Features: {example['features']}, Label: {example['label']}")





import numpy as np


class Neuron:
  def __init__(self, examples):
    np.random.seed(7)
    # Three weights: one for each feature and one more for the bias.
    self.weights = np.random.normal(0, 1, 3 + 1)
    self.examples = examples
    self.train()


  def sigmoid(self, x):
    return 1/(1+np.exp(-x))
  
  def train(self, learning_rate=0.01, batch_size=10000, epochs=200):
    X = [example["features"] + [1] for example in self.examples]
    y = [example["label"] for example in self.examples]

    for _ in range(epochs):
      for i in range(0, len(self.examples), batch_size):
        x_batch = np.array(X[i:i+ batch_size])
        y_batch = np.array(y[i:i+ batch_size])
        y_hat = self.sigmoid(np.dot(self.weights, x_batch.T))
        loss = np.dot((y_hat - y_batch), x_batch)/batch_size
        self.weights -= learning_rate*loss
      
  # Return the probability—not the corresponding 0 or 1 label.
  def predict(self, features):
    features = np.array(features + [1])
    pred = self.sigmoid(np.dot(features, self.weights))
    return pred
    
      

neuron = Neuron(dataset)

# Training the neuron
# neuron.train()
neuron.train(learning_rate=0.1, batch_size=1000, epochs=100)

# Example prediction on a new set of features
new_features = [0.8, 0.2, 0.1]
predicted_prob = neuron.predict(new_features)
print(f"Predicted Probability: {predicted_prob}")



# import numpy as np
# matrix_a = np.array([[1, 2], [3, 4]])
# matrix_b = np.array([[5, 6], [7, 8]])
# result = np.dot(matrix_a, matrix_b)
# print("Matrix A:")
# print(matrix_a)
# print("\nMatrix B:")
# print(matrix_b)
# print("\nResult of dot product:")
# print(result)

