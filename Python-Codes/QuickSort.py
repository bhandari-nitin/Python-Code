###############################
########## Quick Sort #########
###############################

class QuickSort(object):
	def quickSort(self, arr):
		if len(arr) <= 1:
			return arr
		pivot = arr[len(arr) // 2]
		left = [x for x in arr if x < pivot]
		middle = [x for x in arr if x == pivot]
		right = [x for x in arr if x > pivot]
		return self.quickSort(left) + middle + self.quickSort(right)

if __name__ == '__main__':
	q = QuickSort()
	arr = [3, 6, 8, 10, 1, 2, 11]
	print q.quickSort(arr)