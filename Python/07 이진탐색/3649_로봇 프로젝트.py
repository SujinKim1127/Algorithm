import sys
input = sys.stdin.readline

while True:
    try:
        x = int(input())
        n = int(input())
        arr = []
        for _ in range(n):
            arr.append(int(input()))

        arr.sort()
        left = 0
        right = n - 1
        result = 0

        cmTOnano = x * 10000000

        while left < right:
            sum = arr[left] + arr[right]
            if sum > cmTOnano:
                result = 'danger'
                right -= 1
            elif sum < cmTOnano:
                result = 'danger'
                left += 1
            else:
                result = 'yes'
                print('yes', arr[left], arr[right])
                break

        if result == 0 or result == 'danger':
            print('danger')
    except:
        break