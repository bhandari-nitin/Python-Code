# #######
# #######
# Nitin Bhandari
# Deep Learning Foundations 
# Udacity
# This method checks NOT preceptron
##

import pandas as pd

##############################
#### Tune weights and bias ###
##############################

w1 = 2.0
w2 = 3.0
b = 1

# Inputs and Outputs

test_inputs = [(0,0), (0,1), (1,0), (1,1)]
correct_outputs = [0, 1, 1, 0]
outputs = []

# Generate and Check Outputs

for test_input, correct_output in zip(test_inputs, correct_outputs):
	linear_combination = w1 * test_input[0] + w2 * test_input[1] + b
	output = int(linear_combination >= 0)
	is_correct_string = 'Yes' if output == correct_output else 'No'
	outputs.append([test_input[0], test_input[1], linear_combination, output, is_correct_string])

# Print output

num_wrong = len([output[3] for output in outputs if output[3] == 'No'])
output_dataframe = pd.DataFrame(outputs, columns=['Input1', 'Input2', 'Linear Combination', 'Activation Output', 'IsCorrect'])
if not num_wrong:
	print ('Nice! You got it all right. \n')
else:
	print('You got {} wrong. Keep trying'.format(num_wrong))
print (output_dataframe.to_string(index=False))
