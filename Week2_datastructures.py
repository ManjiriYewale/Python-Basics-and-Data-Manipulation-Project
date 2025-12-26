#Lists, Tuples, Dictionary, Set
numbers = [10, 20, 30, 20]
unique_numbers = set(numbers)
print("Unique Numbers:", unique_numbers)

#Function – Sum of Squares
def sum_of_squares(nums):
    return sum(x*x for x in nums)
print(sum_of_squares([1, 2, 3, 4]))

#Lambda Function
square = lambda x: x * x
print(square(5))

#List Comprehension (Filtering)
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = [x for x in numbers if x % 2 == 0]
print(even_numbers)

#Data Cleaning – Remove Duplicates (Client Project)
data = [10, 20, 20, 30, 40, 40, 50]
clean_data = list(set(data))
print("Clean Data:", clean_data)
