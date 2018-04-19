class Node(object):
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None

class BalancedTreeCheck(object):
	def __init__(self, value):
		self.root = Node(value)

	def insert_left(self, value):
		self.left = Node(value)
		return self.left

	def insert_right(self, value):
		self.right = Node(value)
		return self.right

	def is_balanced(self, tree_root):
		if tree_root is None:
			return True
		depths = []  # To store the distinct depths found in the tree
		nodes = []   # To keep the track of nodes visited and their height from the root, so tuple is used
		nodes.append((tree_root, 0))
		while (len(nodes)):
			node, depth = nodes.pop()
			print node.value
			# Case: We found a leaf
			if (not node.left) and (not node.right):
				# We only care about new depth
				if depth not in depths:
					depths.append(depth)
					print depths
					if ((len(depths) > 2) or (len(depths) == 2 and abs(depths[0]-depths[1]) > 1)):
						return False
			else:
				if node.left:
					nodes.append((node.left, depth+1))
				if node.right:
					nodes.append((node.right, depth+1))
		return True

def main():
	# Constructing a Tree
	a = BalancedTreeCheck(5)
	b = a.insert_left(4)
	c = a.insert_right(3)
	d = b.insert_left(2)
	e = b.insert_right(1)
	f = c.insert_left(7)
	g = c.insert_right(8)
	i = d.insert_left(9)
	#j = i.insert_left(10)
	#k = j.insert_left(11)


	print a.is_balanced(a)

if __name__ == "__main__":
	main()
