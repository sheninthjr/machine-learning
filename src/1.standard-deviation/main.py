import numpy as np

data = [10,12,13,12,12,100,12,11,12,13,10]

n = len(data)

mean = sum(data) / n

squared_diff = [(x - mean) ** 2 for x in data]

variance = sum(squared_diff) / n

std_dev = np.sqrt(variance)

print(std_dev)