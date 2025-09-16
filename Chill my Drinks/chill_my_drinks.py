#chill_my_drinks.py
n, m = map(int, input().split())

#그래프 입력 받기
graph = []
for i in range(n):
  graph.append(list(map(int, input())))

def dfs(x, y):

  #debug
  '''
  for row in graph:
    print(row)
  print()
  '''

  if graph[x][y] == True:
    return False

  graph[x][y] = True

  if x-1 >= 0:
    dfs(x-1, y)
  if x+1 < n:
    dfs(x+1, y)
  if y-1 >= 0:
    dfs(x, y-1)
  if y+1 < m:
    dfs(x, y+1)

  return True

result = 0
for i in range(n):
  for j in range(m):
    if dfs(i,j) == True:
      result += 1
      print(1)

print(result)

