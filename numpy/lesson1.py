import numpy as np

# Exercise 1 — Array creation
# 1. Create a NumPy array containing numbers from 10 to 100.
array = np.arange(10, 101)
print(array)
# 2. Create an array containing even numbers from 2 to 50. 
array = np.arange(2 , 51 , 2 )
print(array)
# 3. Create a 3 × 3 matrix filled with zeros. 
array = np.zeros((3,3))
print(array)
# 4. Create a 4 × 4 matrix filled with ones.
array = np.ones((4,4)) 
print(array)
# 5. Generate 10 equally spaced values between 0 and 100.
array = np.linspace(0 , 100 , 10 ) 
print(array)