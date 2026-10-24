limit=int(input("Enter the extreme limit(N): "))

a,b=0,1

print(f"Fibonacci series under {limit}:")
while a<limit:
    print(a, end=" ")
    a,b=b,a+b
print()