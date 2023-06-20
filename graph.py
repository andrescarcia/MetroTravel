
class Graph:
    def __init__(self, vertices):
        # Initialize the graph with the number of vertices
        self.vertices = vertices
        # Create a matrix to represent the edges between vertices
        self.edges = [[float('inf')] * vertices for _ in range(vertices)]
        # Create a set to store the airports that require a visa
        self.visa_required = set()

    def add_edge(self, src, dest, cost):
        # Add an edge between two vertices with a given cost
        self.edges[src][dest] = cost
        self.edges[dest][src] = cost

    def add_visa_required(self, airport):
        # Add an airport to the set of airports that require a visa
        self.visa_required.add(airport)

    def find_route(self, src, dest, has_visa, minimize_cost=True):
        # Find the shortest path between two vertices using Dijkstra's algorithm
        visited = [False] * self.vertices
        dist = [float('inf')] * self.vertices
        dist[src] = 0
        prev = [None] * self.vertices

        for _ in range(self.vertices):
            # Find the vertex with the minimum distance
            u = self.min_distance(dist, visited)
            visited[u] = True

            for v, edge_cost in enumerate(self.edges[u]):
                if not visited[v] and edge_cost != float('inf'):
                    # Check if the user has a visa to enter the airport
                    if not has_visa and v in self.visa_required:
                        continue

                    # Calculate the new cost of the path
                    new_cost = dist[u] + (edge_cost if minimize_cost else 1)
                    if new_cost < dist[v]:
                        # Update the distance and previous vertex
                        dist[v] = new_cost
                        prev[v] = u

        # Return the shortest distance and path
        return (dist[dest], self.build_path(prev, dest))

    def min_distance(self, dist, visited):
        # Find the vertex with the minimum distance
        min_dist = float('inf')
        min_index = -1

        for i, d in enumerate(dist):
            if not visited[i] and d < min_dist:
                min_dist = d
                min_index = i

        return min_index

    def build_path(self, prev, dest):
        # Build the path from the source to the destination
        path = []
        current = dest

        while current is not None:
            path.append(current)
            current = prev[current]

        # Reverse the path and return it
        return path[::-1]
