import random

random_numbers = []

for _ in range(100):
    random_number = random.randint(1, 1000)
    random_numbers.append(random_number)

random_numbers.sort()

for number in random_numbers:
    print(number)