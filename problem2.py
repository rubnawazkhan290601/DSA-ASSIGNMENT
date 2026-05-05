# Array Transformation Cost Minimization

N = int(input())

A = list(map(int, input().split()))

K = int(input())

# Check if transformation is possible
possible = True

for i in range(1, N):
    if (A[i] - A[0]) % K != 0:
        possible = False
        break

if not possible:
    print(-1)

else:
    # Normalize values
    B = [x // K for x in A]

    # Sort to find median
    B.sort()

    median = B[N // 2]

    # Calculate minimum operations
    operations = 0

    for x in B:
        operations += abs(x - median)

    print(operations)