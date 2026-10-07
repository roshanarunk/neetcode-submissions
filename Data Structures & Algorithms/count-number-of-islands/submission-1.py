class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        checked = [[0] * n for _ in range(m)]

        count = 0
        for i in range(m):
            for j in range(n):
                if checked[i][j] == 0 and grid[i][j] == "1":
                    count += 1
                    queue = deque()
                    queue.append((i,j))
                    checked[i][j] = 1
                    while len(queue) > 0:
                        r,c = queue.popleft()
                        
                        for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                            nr, nc = r + dr, c + dc
                            if 0 <= nr < m and 0 <= nc < n:
                                if grid[nr][nc] == "1" and checked[nr][nc] == 0:
                                    checked[nr][nc] = 1
                                    queue.append((nr, nc))
        return count
                    