class change(object):
	def __init__(self):
		self.memo = {}
	def change_possibilites_top_down(self, amount_left, denominations, current_index=0):
		memo_key = ((amount_left, current_index))
		if memo_key in self.memo:
			print "grabbing memo[{}]".format(memo_key)
			return self.memo[memo_key]
		if amount_left == 0:
			return 1
		if amount_left < 0: 
			return 0
		if current_index == len(denominations):
			return 0
		print 'Checking ways to make %i with %s' %(amount_left, denominations[current_index:])
		num_possibilties = 0
		current_coin = denominations[current_index]
		while amount_left >= 0:
			num_possibilties += self.change_possibilites_top_down(amount_left, denominations, current_index+1)
			amount_left -= current_coin
		self.memo[memo_key] = num_possibilties
		return num_possibilties

if __name__ == "__main__":
	c = change()
	answer = c.change_possibilites_top_down(4, [1,2,3])
	print answer