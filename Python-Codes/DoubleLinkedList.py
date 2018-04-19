#################################
###### Dobule Linked List #######
#################################

class Node():
	def __init__(self, data):
		self.data = data
		self.next = None
		self.prev = None

	def getData(self):
		return self.data

	def getNext(self):
		return self.next

	def getPrev(self):
		return self.prev

class DobulyLL():
	def __init__(self):
		self.head = None

	def addNodeAtHead(self, data):
		node1 = Node(data)

		if self.head == None:
			self.head = node1
		else:
			node1.prev = None
			node1.next = self.head
			self.head.prev = node1
			self.head = node1

	def printDLL(self):
		curr = self.head
		while curr:
			print curr.data
			curr = curr.next

	def revPrintDLl(self):
		curr = self.head
		if curr == None:
			print 'No element'
		else:
			while curr.next:
				curr = curr.next
			while curr:
				print curr.data
				curr = curr.prev


def main():
	d = DobulyLL()
	d.addNodeAtHead(5)
	d.addNodeAtHead(6)
	d.addNodeAtHead(7)
	d.addNodeAtHead(8)
	d.addNodeAtHead(9)
	print 'Forward print'
	d.printDLL()
	print 'Reverse print'
	d.revPrintDLl()

if __name__ == '__main__':
	main()
