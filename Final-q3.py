import random

random_numbers = []

for _ in range(100):
    random_number = random.randint(1,10)
    random_numbers.append(random_number)

odd_numbers = [number for number in random_numbers if number % 2 != 0]
print(odd_numbers)