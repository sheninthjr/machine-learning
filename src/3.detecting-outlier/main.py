import numpy as np

data = np.array([10,12,13,12,12,100,12,11,12,13,10])

mean =  np.mean(data)
std_dev = np.std(data)
z_scores = (data - mean) / std_dev

outliers = data[np.abs(z_scores) > 3]

print(outliers)