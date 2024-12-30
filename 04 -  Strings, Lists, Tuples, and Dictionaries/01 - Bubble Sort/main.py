
def bubble_sort(ls):
	for i in range(len(ls)):
		for j in range(len(ls)-1):
			if ls[j] > ls[j+1]:
				ls[j], ls[j+1] = ls[j+1], ls[j]
	return ls

def main():
	ls = [10, 2, 7, 23, 5, 11, 15]
	ls = bubble_sort(ls)
	print(ls)
