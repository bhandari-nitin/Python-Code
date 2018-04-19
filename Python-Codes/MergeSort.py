###################
#### Merge Sort####
###################

#Supporting function for merge sort
def merge(a, b):
	c = []
	while len(a) != 0 and len(b) != 0:
		if a[0] < b[0]:
			c.append(a[0])
			a.remove[a[0]]

		else:
			c.append(b[0])
			c.remove(b[0])

	if len(a) == 0:
		c += b
	else:
		c += a
	return c	


def mergeSort(arr):
	if len(arr) ==0 or len(arr) == 1:
		return arr
	else:
		mid = len(arr)/2
		a = mergeSort(arr[:mid])
		b = mergeSort(arr[mid+1:])
		return merge(a, b)



def main():
	arr = [45, 23, 1, 44, 77, 0 ,3, 121]
	print mergeSort(arr)

if __name__ == '__main__':
	main()