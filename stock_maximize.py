#t = int(input())
#n = int(input())
t = 3
n = 3

str = "1 3 1 2"
a = map(int, str.split())
print(a)

def findProfit(lst):
	max_value = max(lst)
	max_index = lst.index(max_value)
	
	profit = 0
	for i in range(max_index):
		profit -= lst[i]
	profit += lst[max_index] * max_index
	if max_index == len(lst) - 1:
		return profit	
	else:
		return profit + findProfit(lst[max_index+1:])

print(findProfit(a))
