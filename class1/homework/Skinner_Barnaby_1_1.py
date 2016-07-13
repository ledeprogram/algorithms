#Write a function that takes in a list of numbers and outputs the mean of the
#numbers using the formula for mean. Do this without any built-in functions
#like sum(), len(), and, of course, mean()

def mean(list_of_numbers):
    added_numbers = 0
    count = 0
    for number in list_of_numbers:
        added_numbers += number
        count += 1
    return added_numbers / count    
