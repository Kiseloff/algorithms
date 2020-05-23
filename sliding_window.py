def func(arr, k):
    maxSum = sum([arr[i] for i in range(k)])

    for i in range(len(arr) - k):
        currSum = maxSum - arr[i] + arr[i + k]
        maxSum = max(maxSum, currSum)

    return maxSum

if __name__ == '__main__':
    arr = [80,-50,90,100]
    k = 2
    print(func(arr, k))