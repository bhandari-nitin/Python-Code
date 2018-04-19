###################
###InsertionSort###
###################

def insertionSortStandard(list):
	for i in range(1, len(list)):
		key = list[i]
		j = i-1
		while j>=0 and list[j]>key:
			list[j], list[j+1] = list[j+1], list[j]
			j -= 1
	return list

def binaryInsertionSort(list, key, start, end):

	if start == end:
		if list[start] > key:
			return start 
		else:
			return start+1

	if start > end:
		return start

	mid = (start + end)/2

	if list[mid] < key:
		return binaryInsertionSort(list, key, mid+1, end)
	elif list[mid] > key:
		return binaryInsertionSort(list, key, start, mid-1)
	else:
		return mid
 	

#Supporter function for binary insertion sort
def insertionSortBin(list):
	for i in xrange(1, len(list)):
		key = list[i]
		j = binaryInsertionSort(list, key, 0, i-1)
		list = list[:j] + [key] + list[j:i] + list[i+1:]
	return list


if __name__ == '__main__':
	list =  [2, 3, 1, 40, 91, 6, 2, 70]
	#print insertionSortStandard(list)
	print insertionSortBin(list)
