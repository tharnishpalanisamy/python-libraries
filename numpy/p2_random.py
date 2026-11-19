import numpy as np

rng = np.random.default_rng(42)

res = np.random.rand(10) 
print(res)

res = np.random.randint(1, 100 , size=100) 
print(res)