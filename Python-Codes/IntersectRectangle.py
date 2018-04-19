import collections

def intersectRectangle(R1, R2):
	def is_intersect(R1, R2):
		return ( R1.x <= R2.x + R2.width and R1.x + R1.width and
				 R1.y <= R2.y + R2.height and R1.y + R1.height 
			)

	if not is_intersect(R1, R2):
		return Rectangle(0, 0, -1, -1) # No Intersection
		
	return Rectangle(
				max(R1.x, R2.x),
			max(R1.y, R2.y),
			min(R1.x + R1.width, R2.x + R2.width) - max(R1.x, R2.x),
			min(R1.y + R1.height, R2.y + R2.height) - max(R1.y, R2.y))

if __name__ == '__main__':
	
	Rectangle = collections.namedtuple('Rectangle', ('x', 'y', 'width', 'height'))
	R1 = Rectangle(1, 1, 2, 3)
	R2 = Rectangle(2, 2, 3, 3)
	print intersectRectangle(R1, R2)