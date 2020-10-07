# Daniel Ham
# Fibonacci

def fibonacci(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print("Fibonacci numbers")
print("-" * 15)

for i in range(25):
    print(i, ":", fibonacci(i))
