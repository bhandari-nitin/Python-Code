#################
##### Trees #####
#################

class Node(object):
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

class BinaryTree(object):
	def __init__(self, root):
		self.root = Node(root)

	def search_tree(self, find_val):
		return self.preorder_search(tree.root, find_val)

	def print_Tree(self):
		return self.preorder_print(tree.root, "")[:-1]

	def preorder_search(self, start, find_val):
		if start:
			if start.data == find_val:
				return True
			else:
				return self.preorder_search(start.left, find_val) or self.preorder_search(start.right, find_val)
		return False

	def preorder_print(self, start, traversal):
		if start:
			traversal += (str(start.data) + " ")
			traversal = self.preorder_print(start.left, traversal)
			traversal = self.preorder_print(start.right, traversal)
		return traversal

	def postorder_print(self, start, traversal):
		if start:
			traversal = self.postorder_print(start.left, traversal)
			traversal = self.postorder_print(start.right, traversal)
			traversal += (str(start.data) + " ")
		return traversal 



if __name__ == '__main__':
	tree = BinaryTree(1)
	tree.root.left = Node(2)
	tree.root.right = Node(3)
	tree.root.left.left = Node(4)
	tree.root.left.right = Node(5)

	print (tree.search_tree(4))
	print (tree.search_tree(6))

	print (tree.print_Tree())
