import random

num_requests = 1000
max_cylinder = 4999

with open('requests.txt', 'w') as f:
    for _ in range(num_requests):
        request = random.randint(0, max_cylinder)
        f.write(f"{request}\n")
