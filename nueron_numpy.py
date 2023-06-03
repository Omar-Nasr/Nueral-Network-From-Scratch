import numpy as np

## Single nueron
inputs = [1,2,4,2.5]
weights = [0.2,0.8,-0.5,1.0]
bias = 5
output = np.dot(weights,inputs)+bias
print(output)

## Full_layer
inputs = [1,2,3,2.5]
weights = [[0.2,0.8,-0.5,1.0],[1,2,3,4],[-0.26,-0.27,0.17,0.87]]
biases = [2,3,0.5]
output = np.dot(weights,inputs)+biases
print(output)


