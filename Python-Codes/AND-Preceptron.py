####################
###Preceptron-AND###
####################

import pandas as pd

#Setting weights
w1 = 2.0
w2 = 2.0
b = -2.0

test_inputs = [(0,0), (0, 1), (1, 0), (1, 1)]
correct_outputs = [False, False, False, True]
outputs = []

#Generate and check results
for test_input, correct_output in zip(test_inputs, correct_outputs):
	linear_combination = w1 * test_input[0] + w2 *test_input[1] + b 
	output = int(linear_combination>0)
	is_correct_string = 'Yes' if output == correct_output else 'No'
	outputs.append([test_input[0], test_input[1], linear_combination, is_correct_string, correct_output])

#Print output
num_wrong = len([output[3] for output in outputs if output[3] == 'No'])
output_frame = pd.DataFrame(outputs, columns=['Input1', 'Input2', 'Linear Combination', 'Is Correct', 'output'])
if not num_wrong:
	print ('Congrats! You got it all right')
else:
	print ('Sorry, you got {} wrong, Try again'.format(num_wrong))

print (output_frame.to_string(index=False))

