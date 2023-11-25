# 重排九宫格

import numpy as np
import heapq

# 定义九宫格的初始状态和目标状态
grid = np.array([[2, 8, 3], [1, 0, 4], [7, 6, 5]])
target = np.array([[1, 2, 3], [8, 0, 4], [7, 6, 5]])

# 定义移动的四个方向：上、下、左、右
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# 定义状态类
class State:
    def __init__(self, grid, target, cost, parent=None):
        self.grid = grid
        self.target = target
        self.cost = cost
        self.parent = parent

    def __lt__(self, other):
        # 用于优先队列的比较函数
        return self.cost < other.cost

    def get_heuristic(self):
        # 计算曼哈顿距离作为启发式函数
        return np.sum(self.grid != self.target)

# A*算法函数
def astar_search(start, target):
    open_list = []
    closed_set = set()

    heapq.heappush(open_list, start)

    while open_list:
        current_state = heapq.heappop(open_list)

        if np.array_equal(current_state.grid, target):
            # 找到目标状态，返回路径
            path = []
            while current_state:
                path.append(current_state.grid)
                current_state = current_state.parent
            path.reverse()
            return path

        closed_set.add(tuple(map(tuple, current_state.grid)))

        for direction in directions:
            new_grid = current_state.grid.copy()
            zero_pos = np.argwhere(new_grid == 0)[0]
            new_pos = zero_pos + direction

            if not (0 <= new_pos[0] < 3 and 0 <= new_pos[1] < 3):
                continue

            new_grid[zero_pos[0], zero_pos[1]] = new_grid[new_pos[0], new_pos[1]]
            new_grid[new_pos[0], new_pos[1]] = 0

            new_state = State(new_grid, target, current_state.cost + 1, current_state)

            if tuple(map(tuple, new_state.grid)) in closed_set:
                continue

            heapq.heappush(open_list, new_state)

    # 无法找到路径
    return None


# 广度优先搜索算法
def bfs_search(start, target):
    open_list = []
    closed_set = set()

    open_list.append(start)

    while open_list:
        current_state = open_list.pop(0)

        if np.array_equal(current_state.grid, target):
            # 找到目标状态，返回路径
            path = []
            while current_state:
                path.append(current_state.grid)
                current_state = current_state.parent
            path.reverse()
            return path

        closed_set.add(tuple(map(tuple, current_state.grid)))

        for direction in directions:
            new_grid = current_state.grid.copy()
            zero_pos = np.argwhere(new_grid == 0)[0]
            new_pos = zero_pos + direction

            if not (0 <= new_pos[0] < 3 and 0 <= new_pos[1] < 3):
                continue

            new_grid[zero_pos[0], zero_pos[1]] = new_grid[new_pos[0], new_pos[1]]
            new_grid[new_pos[0], new_pos[1]] = 0

            new_state = State(new_grid, target, current_state.cost + 1, current_state)

            if tuple(map(tuple, new_state.grid)) in closed_set:
                continue

            open_list.append(new_state)

    # 无法找到路径
    return None


# 深度优先搜索算法
def dfs_search(start, target):
    open_list = []
    closed_set = set()

    open_list.append(start)

    while open_list:
        current_state = open_list.pop(0)

        if np.array_equal(current_state.grid, target):
            # 找到目标状态，返回路径
            path = []
            while current_state:
                path.append(current_state.grid)
                current_state = current_state.parent
            path.reverse()
            return path

        closed_set.add(tuple(map(tuple, current_state.grid)))

        for direction in directions:
            new_grid = current_state.grid.copy()
            zero_pos = np.argwhere(new_grid == 0)[0]
            new_pos = zero_pos + direction

            if not (0 <= new_pos[0] < 3 and 0 <= new_pos[1] < 3):
                continue

            new_grid[zero_pos[0], zero_pos[1]] = new_grid[new_pos[0], new_pos[1]]
            new_grid[new_pos[0], new_pos[1]] = 0

            new_state = State(new_grid, target, current_state.cost + 1, current_state)

            if tuple(map(tuple, new_state.grid)) in closed_set:
                continue

            open_list.insert(0, new_state)

    # 无法找到路径
    return None


if __name__ == '__main__':
    # 创建初始状态
    start_state = State(grid, target, 0)

    # 运行A*算法
    import time
    start_time = time.time()
    path = astar_search(start_state, target)
    end_time = time.time()
    print("运行时间：", end_time - start_time)
    print("移动步数：", len(path) - 1)
    if path:
        print("找到路径：")
        for state in path:
            print(state)
    else:
        print("无法找到路径")

    # 运行广度优先搜索算法
    start_time = time.time()
    path = bfs_search(start_state, target)
    end_time = time.time()
    print("运行时间：", end_time - start_time)
    print("移动步数：", len(path) - 1)
    if path:
        print("找到路径：")
        for state in path:
            print(state)
    else:
        print("无法找到路径")

    # 运行深度优先搜索算法
    start_time = time.time()
    path = dfs_search(start_state, target)
    end_time = time.time()
    print("运行时间：", end_time - start_time)
    print("移动步数：", len(path) - 1)
    if path:
        print("找到路径：")
        for state in path:
            print(state)
    else:
        print("无法找到路径")
