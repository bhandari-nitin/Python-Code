from sets import Set
from random import choice

def chance_of_visiting_all_states(iterations, k, n=24):
	r = range(n)
	total = 0
	for i in range(iterations):
		s = Set()
		for j in range(k):
			s.add(choice(r))
			if len(s) == n:
				total += 1
				break
	return float(total)/iterations

steps = 1000
print 'Chance of visiting all states in {st} steps: {ch}'.format(st=steps, ch=chance_of_visiting_all_states(2000, steps, 96))