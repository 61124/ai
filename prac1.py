from collections import deque

class Graph:
    def __init__(self, V):  # <-- fixed __init__
        self.V = V
        self.adj = [[] for i in range(V)]

    def add_edge(self, v, w):
        self.adj[v].append(w)
        self.adj[w].append(v)  # undirected graph

    def dfs_util(self, v, target, visited):
        visited[v] = True
        print(v, end=" ")
        if v == target:
            return True
        for neighbor in self.adj[v]:
            if not visited[neighbor]:
                if self.dfs_util(neighbor, target, visited):
                    return True
        return False

    def dfs(self, start, target):
        visited = [False] * self.V
        self.dfs_util(start, target, visited)

    # Recursive BFS Helper
    def bfs_util(self, q, visited, target):
        if not q:
            return

        v = q.popleft()
        print(v, end=" ")

        if v == target:
            return

        for neighbor in self.adj[v]:
            if not visited[neighbor]:
                visited[neighbor] = True
                q.append(neighbor)

        self.bfs_util(q, visited, target)

    def bfs(self, start, target):
        visited = [False] * self.V
        q = deque()
        visited[start] = True
        q.append(start)
        self.bfs_util(q, visited, target)


def main():
    flag = True
    while flag:
        V = int(input("Enter the number of vertices (0 to exit): "))
        if V == 0:
            flag = False
            break

        g = Graph(V)

        E = int(input("Enter the number of edges: "))
        print("Enter edges (source destination):")
        for _ in range(E):
            src, dest = map(int, input().split())
            g.add_edge(src, dest)

        start = int(input("Enter start vertex: "))
        target = int(input("Enter target vertex: "))

        print("Select: 1.DFS 2.BFS 3.End: ", end="")
        choice = int(input())

        if choice == 1:
            print("DFS Traversal: ", end="")
            g.dfs(start, target)
            print()
        elif choice == 2:
            print("BFS Traversal: ", end="")
            g.bfs(start, target)
            print()
        elif choice == 3:
            print("Thank you!")
            flag = False
        else:
            print("Wrong choice!")

if __name__ == "__main__":  # <-- fixed __name__ and __main__
    main()