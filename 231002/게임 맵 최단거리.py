#전형적인 BFS 풀이이므로 BFS에 대한 부분은 설명을 생략하고, distance를 구하는 부분만 주의 깊게 살펴보면 될 것 같다. 트리에서 자식 노드의 거리는 부모 노드의 거리 + 1이므로 각 노드의 거리를 딕셔너리로 저장해놨다가 불러오면 된다.
#이 문제는 최단 경로를 찾는 문제로 BFS와 DFS 중 BFS가 더 유리하다.
#그 이유는 DFS는 모든 경로를 탐색한 후 거리를 비교해야하는 반면 BFS는 탐색 도중 타겟이 발견되면 바로 종료할 수 있기 때문이다.


from collections import deque

def solution(maps):
    n, m = len(maps), len(maps[0])
    visited = [[False for _ in range(m)] for _ in range(n)]
    return bfs(maps, 0, 0, visited)
    
def bfs(maps, x, y, visited):
    n, m = len(maps), len(maps[0])
    queue = deque([(x, y)])
    visited[x][y] = True
    distance = {(x, y): 0}
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<m and not visited[nx][ny] and maps[nx][ny]:
                if (nx, ny) == (n-1, m-1): return distance[(x, y)] + 2
                queue.append((nx, ny))
                distance[(nx, ny)] = distance[(x, y)] + 1
                visited[nx][ny] = True
    return -1