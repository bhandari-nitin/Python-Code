##########################################
##### Reversing a string using Stack #####
##########################################
from array import array

class Stack():
	
	def __init__(self):
		self.items = []

	def push(self, data):
		return self.items.insert(0, data)

	def pop(self):
		return self.items.pop(0)

	def peek(self):
		return self.items[0]

	def isEmpty(self):
		return len(self.items) == 0

def reverseString(text):

	s = Stack()
	for c in text:
		s.push(c)
	rev_str = []
	while not s.isEmpty():
		rev_str.append(s.pop())
	array 


if __name__ == '__main__':
	print reverseString('Autobahn Motowreks')