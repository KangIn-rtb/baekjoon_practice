# UOSPC 세기

n = int(input())
s = input()
uospc = [0]*(5)
for i in s:
    if i == 'u':
        uospc[0] += 1
    if i == 'o':
        uospc[1] += 1
    if i == 's':
        uospc[2] += 1
    if i == 'p':
        uospc[3] += 1
    if i == 'c':
        uospc[4] += 1
print(min(uospc))