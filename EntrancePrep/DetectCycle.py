def CycleDetection(arr):
    n = len(arr)
    for length in range(1, n//2+1):
        isCycle = True
        for i in range(n- length):
            if arr[i] != arr[i + length]:
                isCycle = False
                break
        if isCycle:
            print('Cycle Detected!')
            return length        
    return -1
arr =[1,2,1,2,1]
print(f'The length of the cycle is: {CycleDetection(arr)}')