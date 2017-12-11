# n = int(input().strip())
n = 15
b = bin(n)
lens = len(b)
i = 2
maxlengh = 0
curlen = 0
while (i < lens):
    if b[i] == '0':
        curlen = 0
    if b[i] == '1':
        curlen += 1
    if maxlengh < curlen:
        maxlengh = curlen
    i += 1
print(maxlengh)
print(b)
