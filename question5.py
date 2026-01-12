from collections import deque
import heapq

# -----------------------------
# BREADTH FIRST SEARCH (BFS)
# -----------------------------
def BFS(graph, start):
    visited = set([start])
    queue = deque([start])
    order = []

    while queue:
        node = queue.popleft()
        order.append(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return order


# -----------------------------
# DEPTH FIRST SEARCH (DFS)
# -----------------------------
def DFS(graph, start):
    visited = set()
    order = []

    def dfs(node):
        visited.add(node)
        order.append(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor)

    dfs(start)
    return order


# -----------------------------
# DEPTH LIMITED SEARCH (DLS)
# -----------------------------
def DLS(graph, start, goal, limit):
    visited = set()

    def dls(node, depth):
        if node == goal:
            return True
        if depth == limit:
            return False

        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                if dls(neighbor, depth + 1):
                    return True
        return False

    return dls(start, 0)


# -----------------------------
# ITERATIVE DEEPENING SEARCH (IDS)
# -----------------------------
def IDS(graph, start, goal, max_depth):
    for depth in range(max_depth + 1):
        visited = set([start])
        if DLS_util(graph, start, goal, depth, visited):
            return f"Goal found at depth {depth}"
    return "Goal not found"


def DLS_util(graph, node, goal, depth, visited):
    if depth == 0 and node == goal:
        return True
    if depth > 0:
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                if DLS_util(graph, neighbor, goal, depth - 1, visited):
                    return True
    return False


# -----------------------------
# UNIFORM COST SEARCH (UCS)
# -----------------------------
def UCS(graph, start, goal):
    pq = [(0, start)]
    visited = set()

    while pq:
        cost, node = heapq.heappop(pq)

        if node == goal:
            return cost

        if node in visited:
            continue

        visited.add(node)

        for neighbor, weight in graph[node]:
            if neighbor not in visited:
                heapq.heappush(pq, (cost + weight, neighbor))

    return float('inf')


# -----------------------------
# USER INPUT SECTION
# -----------------------------
def input_unweighted_graph():
    graph = {}
    n = int(input("Enter number of vertices: "))

    for _ in range(n):
        node = input("Enter vertex name: ")
        neighbors = input(f"Enter neighbors of {node} (space separated): ").split()
        graph[node] = neighbors

    return graph


def input_weighted_graph():
    graph = {}
    n = int(input("Enter number of vertices: "))

    for _ in range(n):
        node = input("Enter vertex name: ")
        edges = input(
            f"Enter neighbors and weights of {node} (format: neighbor,weight): "
        ).split()

        graph[node] = []
        for edge in edges:
            neighbor, weight = edge.split(',')
            graph[node].append((neighbor, int(weight)))

    return graph


# -----------------------------
# MAIN MENU
# -----------------------------
def main():
    print("\nGRAPH SEARCH ALGORITHMS")
    print("1. BFS")
    print("2. DFS")
    print("3. DLS")
    print("4. IDS")
    print("5. UCS")

    choice = int(input("Choose an option: "))

    if choice in [1, 2, 3, 4]:
        graph = input_unweighted_graph()
        start = input("Enter start node: ")

    if choice == 1:
        print("BFS Order:", BFS(graph, start))

    elif choice == 2:
        print("DFS Order:", DFS(graph, start))

    elif choice == 3:
        goal = input("Enter goal node: ")
        limit = int(input("Enter depth limit: "))
        print("Goal Found:", DLS(graph, start, goal, limit))

    elif choice == 4:
        goal = input("Enter goal node: ")
        max_depth = int(input("Enter maximum depth: "))
        print(IDS(graph, start, goal, max_depth))

    elif choice == 5:
        graph = input_weighted_graph()
        start = input("Enter start node: ")
        goal = input("Enter goal node: ")
        cost = UCS(graph, start, goal)
        print("Minimum Cost:", cost)

    else:
        print("Invalid choice!")


# -----------------------------
# PROGRAM ENTRY POINT
# -----------------------------
if __name__ == "__main__":
    main()
