import matplotlib.pyplot as plt

# 1차 함수
x = [a for a in range(0, 11)]
y = list(range(0, 11))

print('x축', x)
print('y축', y)

plt.plot(x, y)
plt.show()

# 2차 함수
# f(x) = x^2
f = lambda x: x**2

x = [a for a in range(-10, 10)]
y = [f(y) for y in range(-10, 10)]

print('x축', x)
print('y축', y)

plt.plot(x, y)
plt.show()