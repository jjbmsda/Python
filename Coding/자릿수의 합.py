import sys
sys.stdin=open("input.txt", "r")
def digit_sum(x):
    sum = 0
    for i in str(x):
        sum += int(i)
    return sum

n=int(input())
a=list(map(int, input().split()))
max = 0
res = 0

for i in a:
    tot = digit_sum(i)
    if tot > max:
        max = tot
        res = i

print(res)        
    
    
