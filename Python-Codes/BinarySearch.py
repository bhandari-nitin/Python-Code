###########################
###### Binary Search ######
###########################

def binary_search(array, value):
	floor_index = 0
	ceiling_index = len(array) - 1
	
	while floor_index <= ceiling_index:
		mid = (floor_index + ceiling_index) / 2
		if array[mid] == value:
			return True
		elif array[mid] < value:
			floor_index = mid + 1
		else:
			ceiling_index = mid - 1
	return False

if __name__ == '__main__':
	array_list = [10, 20, 30 , 40, 50]
	print binary_search([], 40)
