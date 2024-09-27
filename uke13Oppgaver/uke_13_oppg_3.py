import numpy as np

xs = [[83, 1, 22], [117, 52, 3], [14, 42, 784]]

arr = np.array(xs) #pirate arr

for item in arr[1:]:
    print(item[:1])
