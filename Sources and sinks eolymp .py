# https://www.eolymp.com/en/problems/3986

n = int(input())
adj_matrix = []
for _ in range(n):
    row = list(map(int, input().split()))
    adj_matrix.append(row)

sources = []
sinks = []

for i in range(n):
    is_source = True
    is_sink = True
    for j in range(n):
        if adj_matrix[j][i] == 1:
            is_source = False
        if adj_matrix[i][j] == 1:
            is_sink = False
    if is_source:
        sources.append(i + 1)
    if is_sink:
        sinks.append(i + 1)

print(len(sources), end=' ')
print(' '.join(map(str, sources)))
print(len(sinks), end=' ')
print(' '.join(map(str, sinks)))
