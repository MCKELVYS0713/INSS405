def get_input_numbers(num_inputs):
    numbers = []
    for _ in range (num_inputs):
        number = float(input("Enter a number: "))
        numbers.append(number)
    return numbers

def calculate_sum(numbers):
    total= sum(numbers)
    return total

def calculate_median(numbers):
    sorted_numbers = sorted(numbers)
    n = len (sorted_numbers)
    if n % 2 == 0:
        mid1 = (sorted_numbers[n // 2 -1] + sorted_numbers[n // 2]) / 2
    else:
        median = sorted_numbers[n // 2]
    return median

num_inputs = 10
input_numbers = get_input_numbers(num_inputs)

sum_numbers = calculate_sum(input_numbers)
median = calculate_median(input_numbers)



print("Numbers:", input_numbers)
print("Mean:", mean)
print("Sum:", sum_numbers)
print("Median:", median)