import numpy as np
X = np.array([[1,2,3,2.5],[2.0,5.0,-1.0,2.0],[-1.5,2.7,3.3,-0.8]])
# weights = [[0.2,0.8,-0.5,1.0],
#     [0.5,-0.91,0.26,-0.5],
#     [-0.26,-0.27,0.17,0.87]]
# weights=np.transpose(np.array(weights))
# print(weights.shape)
# print(inputs.shape)
# biases = [2,3,0.5]
# output_layer1 = np.dot(inputs,weights)+biases
# print(output_layer1)
# weights_2 = [[0.1,0.14,0.5],
#     [-0.5,0.12,-0.33],
#     [-0.44,0.73,-0.13]]
# biases_2 = [-1,2,-0.5]
# output_layer2 = np.dot(output_layer1,weights_2)+biases_2
# print(output_layer2)

## Converting to an object

class Layer_Dense:
    def __init__(self,n_inputs,n_neurons):
        self.weights = 0.1*np.random.randn(n_inputs,n_neurons)
        self.biases = np.zeros((1,n_neurons))
    def forward(self,inputs):
        self.output = np.dot(inputs,self.weights)+self.biases
layer1 = Layer_Dense(X.shape[1],3)

layer1.forward(X)
layer2 = Layer_Dense(layer1.output.shape[1],3)
layer2.forward(layer1.output)
print(layer1.output)
print(layer2.output)
