from ui import MetroTravelUI
from graph import Graph

def main():
    # Define the airport codes and create a dictionary to map them to indices
    airport_codes = ["CCS", "AUA", "CUR", "BON", "SDQ", "SXM", "SBH", "POS", "BGI", "PTP", "FDF"]
    airport_indices = {code: i for i, code in enumerate(airport_codes)}

    # Create a graph with the number of vertices equal to the number of airports
    graph = Graph(len(airport_codes))

    # Define the edges between airports and their costs
    edges = [
        ("CCS", "AUA", 40),
        ("CCS", "CUR", 35),
        ("CCS", "BON", 60),
        ("AUA", "CUR", 15),
        ("AUA", "BON", 15),
        ("CUR", "BON", 15),
        ("CCS", "SDQ", 180),
        ("SDQ", "SXM", 50),
        ("SXM", "SBH", 45),
        ("CCS", "POS", 150),
        ("CCS", "BGI", 180),
        ("POS", "BGI", 35),
        ("POS", "SXM", 90),
        ("BGI", "SXM", 70),
        ("POS", "PTP", 80),
        ("POS", "FDF", 75),
        ("PTP", "SXM", 100),
        ("PTP", "SBH", 80),
        ("CUR", "SXM", 80),
        ("AUA", "SXM", 85),
    ]

    # Add the edges to the graph
    for src, dest, cost in edges:
        graph.add_edge(airport_indices[src], airport_indices[dest], cost)

    # Define the airports that require a visa and add them to the graph
    visa_required = ["AUA", "BON", "CUR", "SXM", "SDQ"]
    for airport in visa_required:
        graph.add_visa_required(airport_indices[airport])

    # Create a MetroTravelUI object and run the application
    app = MetroTravelUI(graph, airport_codes)
    app.run()

if __name__ == "__main__":
    main()