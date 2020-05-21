def bsearch(scope, goal):
    scope.sort()
    start, end = 0, len(scope) - 1

    while (start != end):
        middle = int((start + end) / 2)
        if scope[middle] == goal:
            return middle
        elif scope[middle] > goal:
            end = middle
        else:
            start = middle + 1

    return start if scope[start] == goal else None

if __name__ == '__main__':
    foo = [7,6,44,1,4,7,99,0,12,43]
    goal = 7
    print(bsearch(foo, goal))