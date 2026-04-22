import numpy as np

# ------------------------------
# Activity 1
# ------------------------------
a = np.array([1, 2, 3, 4, 5])
b = np.array([10, 20, 30])
c = np.array([[1, 2], [3, 4]])

print("a-Array:", a)
print("b-Array:", b)
print("c-Array:", c)
print("Type of a:", type(a))
print("Data type of a:", a.dtype)

# ------------------------------
# Activity 2
# ------------------------------
x = np.array([[1, 2, 3], [4, 5, 6]])

print("Shape of x:", x.shape)
print("Size of x:", x.size)
print("Number of Dimensions of x:", x.ndim)
print("Data type of x:", x.dtype)

# ------------------------------
# Activity 3
# ------------------------------
q = np.array([5, 10, 15, 20, 25])

print("First Value:", q[0])
print("Third Value:", q[2])
print("Last Value:", q[-1])

e = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

print("Value 2:", e[0, 1])
print("Value 6:", e[1, 2])
print("Value 8:", e[2, 1])
print("Entire First Row:", e[0, :])
print("Entire Second Column:", e[:, 1])

# ------------------------------
# Activity 4
# ------------------------------
r = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

print("Values from index 2 to 6:", r[2:7])
print("First 5 values:", r[0:5])
print("Last 3 values:", r[-3:])
print("Every second value:", r[::2])

# ------------------------------
# Activity 5
# ------------------------------
z = np.array([1, 2, 3, 4, 5])
z[2] = 99
print("Updated z:", z)

u = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
u[1, 1] = 50
print("Updated u:\n", u)

# ------------------------------
# Activity 6
# ------------------------------
y = np.zeros(5)
print("Zeros:", y)

i = np.ones(4)
print("Ones:", i)

arr = np.arange(10)
print("Arange:", arr)

arr = np.linspace(0, 1, 5)
print("Linspace:", arr)