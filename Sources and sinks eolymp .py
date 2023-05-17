# https://www.eolymp.com/en/problems/3986

n = int(input())
adj_matrix = []
for _ in range(n):
    row = list(map(int, input().split()))
    adj_matrix.append(row)

sources = []
sinks = []

for i in range(1, n+1):
    is_source = True
    is_sink = True
    for j in range(1, n+1):
        if adj_matrix[j-1][i-1] == 1:
            is_source = False
        if adj_matrix[i-1][j-1] == 1:
            is_sink = False
    if is_source:
        sources.append(i)
    if is_sink:
        sinks.append(i)

print(len(sources), *sources)
print(len(sinks), *sinks)
