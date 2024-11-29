n = 5
for i in range(n, 0, -1):
    print((n-i)*' '+ i * '*' )
for i in range(n):
    print((n-i)*'*')

#stair-case pattern
def pattern(n):
    for i in range(1,n+1):
        k = i+1 if ( i%2 != 0) else i
        for j in range(k,n):
            if j>=k:
                print(end=" ")
        for l in range(0,k):
            if l == k - 1:
                print('*')
            else:
                print('*', end=" ")
pattern(8)

#double-sided staircase
def pattrn(h):
    for i in range(1, h+1):
        for j in range(i):
            print('*', end="")
        print(' ' * (2 * h - 2 * i), end="")
        for j in range(i):
            print('*', end="")
        print()
pattrn(6)

