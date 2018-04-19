##################################
###### Binary Search Trees #######
##################################

class Node(object):
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None

class BinaryTree(object):
	def __init__(self, root):
		self.root = Node(root)

	def insertBST(self, new_val):
		print tree.root
		return self.insertHelper(tree.root, new_val)

	def insertHelper(self, start, new_val):
		if start.value > new_val:
			if start.left:
				self.insertHelper(start.left, new_val)
			else:
				start.left = Node(new_val)
		else:
			if start.right:
				self.insertHelper(start.right, new_val)
			else:
				start.right = Node(new_val)

	def search(self, find_val):
		return self.searchHelper(tree.root, find_val)

	def searchHelper(self, start, find_val):
		if start:
			if start.value == find_val:
				return True
			elif start.value < find_val:
				return searchHelper(start.right, find_val)
			else:
				return searchHelper(start.left, find_val)
		return False

	def printBST(self):
		return self.printHelper(tree.root, '')

	def printHelper(self, start, traversal):
		if start:
			traversal +=  (str(start.value) + ' ')
			traversal = self.printHelper(start.left, traversal)
			traversal = self.printHelper(start.right, traversal)
		return traversal


if __name__ == '__main__':
	tree = BinaryTree(10)
	tree.insertBST(6)
	tree.insertBST(20)
	tree.insertBST(8)
	tree.insertBST(25)

	print (tree.printBST())