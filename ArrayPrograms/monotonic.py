def monotonic(A):
    return (all(A[i] >= A[i+1] for i in range(len(A)-1))) or all(A[i] <= A[i+1] for i in range(len(A)-1))

if __name__ == '__main__':
    arr = [1,2,3,4,4]
    print(monotonic(arr))
