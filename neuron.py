inputs = [1,2,3] #inputs of our first neuron
weights = [0.2,0.8,-0.5] #bias of our first neuron
bias = 2 #bias of our first neuron 
output = inputs[0]*weights[0]+inputs[1]*weights[1]+inputs[2]*weights[2]+bias
#formula for a single neuron is sum of inputs*weights + bias
print(output)
## Modeling 3 neurons with 4 inputs 
inputs = [1,2,3,2.5]
weight1 = [0.2,0.8,-0.5,1.0]
weight2 = [0.5,-0.91,0.26,-0.5]
weight3 = [-0.26,-0.27,0.17,0.87]
weights = [[0.2,0.8,-0.5,1.0],
    [0.5,-0.91,0.26,-0.5],
    [-0.26,-0.27,0.17,0.87]]
biases = [2,3,0.5]
bias1 = 2 
bias2 = 3 
bias3 = 0.5
layer_outputs=[]
#cleaner way to calculate 
for nueron_weights,nueron_bias in zip(weights,biases):
    nueron_output=0
    for n_input,weight in zip(inputs,nueron_weights):
        nueron_output+=n_input*weight
    nueron_output+=nueron_bias
    layer_outputs.append(nueron_output)



#formula for a single neuron is sum of inputs*weights + bias

output = [

inputs[0]*weight1[0]+inputs[1]*weight1[1]+inputs[2]*weight1[2]+inputs[3]*weight1[3]+bias1,

inputs[0]*weight2[0]+inputs[1]*weight2[1]+inputs[2]*weight2[2]+inputs[3]*weight2[3]+bias2,

inputs[0]*weight3[0]+inputs[1]*weight3[1]+inputs[2]*weight3[2]+inputs[3]*weight3[3]+bias3
]




