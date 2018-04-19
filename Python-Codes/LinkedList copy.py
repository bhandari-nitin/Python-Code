class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

class linkedList:
	
	def __init__(self):
		self.head = None

	def addElement(self, data):
		
		node = Node(data)
		
		if self.head == None:
			self.head = node
		else:
			node.next = self.head
			node.next.prev = node
			self.head = node
		return self.head

	def traverseList(self):
		current = self.head
		while current:
			print current.data
			current = current.next

	def searchList(self, k):
		current = self.head
		previous = None
		found = False    #Setting the flag
		while current != None and found != True:
			if current.data == k:
				found = True
			else:
				previous = current
				current = current.next
		return found, previous, current

	def delElement(self, k):
		
		a= self.searchList(k)
		isPresent = a[0] 
		prev = a[1]
		current = a[2]

		if isPresent == False:
			print 'Element does not exists'
		else:
			if prev == None:
				temp = self.head
				self.head = temp.next
				temp.next = None
			else :
				prev.next = current.next
				current.next = None
				
		self.traverseList()

	def insertAfter(self, previous_node, new_data):
		node2 = Node(new_data)
		if previous_node == None:
			temp = self.head
			node2 = self.head 
			node2.next = temp.next
		else:
			node2.next = previous_node.next
			previous_node.next = node2

	def reverseListBiIterate(self):
		current = self.head
		prev = None
		next = None
		while current:
			next = current.next
			current.next = prev
			prev = current 
			current = next
		self.head = prev
		self.traverseList()

	def printElementsUsingRecursion(self, head):
		if head != None:
			self.printElementsUsingRecursion(head.next) 
			print head.data

	def reveserListUsingRecursion(self, curr, prev):
		if curr.next is None:
			self.head = curr
			curr.next = prev 
			return
		next = curr.next
		curr.next = prev
		self.reveserListUsingRecursion(next, curr)

if __name__ == '__main__':
	
	l = linkedList()
	a = l.addElement('a')
	b = l.addElement('b')
	c = l.addElement('c')
	d = l.addElement('d')
	e = l.addElement('e')
	f = l.addElement('i')
	g = l.addElement('f')
	print g
	#l.reverseListBiIterate()
	#l.printElementsUsingRecursion(g)
	print 'before recursion'
	print l.traverseList()
	l.reveserListUsingRecursion(g, None)
	print 'after recursion'
	print l.traverseList()











