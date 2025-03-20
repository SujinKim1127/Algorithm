n = int(input())

min = 1
max = n

while 1: 
  mid = (min + max) / 2
  double = mid * mid
  if(double == n): 
    print(mid) 
    break
  elif (double < n):
    min = mid + 1
  elif (double > n):
    max = mid - 1
