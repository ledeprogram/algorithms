def my_mean(list):
	length = count_length(list)
	sum = 0
	for i in list:
		sum = sum + i
	return sum / length

def count_length(list):
	count = 0
	for i in list:
		if i == '':
			break
		else:
			count += 1
	return count

numbers = [1,2,3,4,5,6,7,8,9]
print(my_mean(numbers))
