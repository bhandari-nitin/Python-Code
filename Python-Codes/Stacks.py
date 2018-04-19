##################
##### Stacks #####
##################

#Python prevents the interpreter stack from growing larger than sys.getrecursionlimit().
#When you hit that limit you get the RuntimeError

class stack():
	def __init__(self):
		self.items = [] #Stack empty instance

	def push(self, data):
		return self.items.insert(0, data)    #Using .append will make it a queue

	def pop(self):
		return self.items.pop(0)    #index 0 for removing the last element

	def peek(self):
		return self.items[0] # returns the top of the stack

	def size(self):
		return len(self.items)

	def printStack(self):
		print 'Elements in stack are:'
		for i in self.items:
			print i

def run():
	s = stack()
	s.push(10)
	s.push(20)
	s.push(30)
	print s.printStack()
	print 'Top is: {}'.format(s.peek())
	s.pop()
	print 'Top after performomg pop is: {}'.format(s.peek())
	print s.printStack()

if __name__ == '__main__':
	run()
