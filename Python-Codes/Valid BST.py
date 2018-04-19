class Node(object):
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None

class BST(object):
	def __init__(self, root_val):
		self.root = Node(root_val)

	def insert(self, new_value):
		return self.insert_helper(tree.root, new_value)

	def insert_helper(self, start, new_value):
		if start.value > new_value:
			if start.left:
				self.insert_helper(start.left, new_value)
			else:
				start.left = Node(new_value)
		else:
			if start.right:
				self.insert_helper(start.right, new_value)
			else:
				start.right = Node(new_value)

	def inoder_traversal(self, start):
		if start:
			if start.left:
				self.inoder_traversal(start.left)
			print start.value
			if start.right:
				self.inoder_traversal(start.right)

	def print_BST(self, start):
		if start:
			print start.value
			self.print_BST(start.left)
			self.print_BST(start.right)

	def is_valid_BST(self, start):
		# Using DFS
		# DFS needs space proportional to depth of tree, depth = log(n), where n is the number of the nodes in the tree
		# Can use inorder travesal, result is accending order and if it is sorted that way, BOOM!, you got the answer
		# But use inorder if you dont have to save the entire list of values of the nodes
		nodes = []
		nodes.append((start, -float('inf'), float('inf')))
		while len(nodes):
			node, lower_bound, upper_bound = nodes.pop()
			if node.value < lower_bound or node.value > upper_bound:
				return False
			if node.left:
				nodes.append(node.left, lower_bound, node.value)
			if node.right:
				nodes.append(node.right, node.value, upper_bound)
		return True




if __name__ == "__main__":
	tree = BST(20)
	tree.insert(15)
	tree.insert(25)
	tree.insert(10)
	tree.insert(17)
	tree.insert(23)
	tree.insert(30)
	tree.insert(5)
	tree.insert(14)
	tree.insert(16)
	tree.insert(18)
	tree.insert(22)
	tree.insert(24)
	tree.insert(29)
	tree.insert(35)
	#tree.print_BST(tree.root)
	print tree.inoder_traversal(tree.root)
	