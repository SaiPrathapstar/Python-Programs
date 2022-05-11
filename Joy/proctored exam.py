m = list(map(int, input().split()))
m.sort()
count = 0
n = []
j = len(m) - 1
while sum(m) > sum(n):
  n.append(m[j])
  m.pop(j)
  j -= 1
  count += 1
print(count , end = "")