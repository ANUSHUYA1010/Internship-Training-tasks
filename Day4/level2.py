print("21. Linear Algebra")
import numpy as np
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print("Vector A:", a)
print("Vector B:", b)
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Dot Product:", np.dot(a, b))
print("\n22. Matrix Multiplication")
A = np.array([[1, 2],[3, 4]])
B = np.array([[5, 6],[7, 8]])
C = np.matmul(A, B)
print("Matrix Multiplication:")
print(C)
print("\n23. Probability")
total_cards = 52
ace_cards = 4
probability = ace_cards / total_cards
print("Probability of getting an Ace:", probability)
print("\n24. Conditional Probability")
P_A_and_B = 0.2
P_B = 0.5
P_A_given_B = P_A_and_B / P_B
print("Conditional Probability P(A|B):", P_A_given_B)
print("\n25. Mean and Variance")
data = np.array([10, 20, 30, 40, 50])
print("Mean:", np.mean(data))
print("Variance:", np.var(data))
print("Standard Deviation:", np.std(data))
print("\n26. Gradient Descent")
x = 5
learning_rate = 0.1
gradient = 2 * x
new_x = x - learning_rate * gradient
print("Old x:", x)
print("Gradient:", gradient)
print("Updated x:", new_x)
print("\n27. Loss Function")
y_true = np.array([10, 20, 30, 40])
y_pred = np.array([12, 18, 29, 41])
mse = np.mean((y_true - y_pred) ** 2)
print("Mean Squared Error:", mse)
print("\n28. Derivatives")
x = int(input())
derivative = 2 * x
print("Derivative at x =", x, "is", derivative)
print("\n29. Optimization")
x = np.linspace(-5, 5, 100)
y = x**2
minimum = np.min(y)
print("Minimum Value:", minimum)
print("\n30. Implement Gradient Descent")
# Minimize f(x) = x^2
x = int(input())
learning_rate = 0.1
iterations = 50
for i in range(iterations):
    gradient = 2 * x
    x = x - learning_rate * gradient
print("Optimized x:", x)
print("Minimum value:", x**2)