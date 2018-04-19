##################################
########## Prime Numbers #########
##################################

def prime_num(start, end):
	prime_list = []
	if start == 1 or start == 0:
		start = 2
	else:
		for x in range(start, end):
			if all(x%j for j in range(2, x)):
				prime_list.append(x)
	return prime_list

print prime_num(0, 10)
