from queue import Queue
import tkinter as tk
from graph import Graph
from dibujar import agregar_arista
import networkx as nx
import matplotlib.pyplot as plt

class MetroTravelUI:
    def __init__(self, graph, airport_codes, edges):
        self.graph = graph
        self.airport_codes = airport_codes
        self.edges= edges
        self.root = tk.Tk()
        self.root.title("Metro Travel")

        self.origin_label = tk.Label(self.root, text="Origen:")
        self.origin_label.grid(row=0, column=0)
        self.origin_entry = tk.Entry(self.root)
        self.origin_entry.grid(row=0, column=1)

        self.destination_label = tk.Label(self.root, text="Destino:")
        self.destination_label.grid(row=1, column=0)
        self.destination_entry = tk.Entry(self.root)
        self.destination_entry.grid(row=1, column=1)

        self.visa_var = tk.BooleanVar()
        self.visa_check = tk.Checkbutton(self.root, text="Tiene visa", variable=self.visa_var)
        self.visa_check.grid(row=2, column=0, columnspan=2)

        self.result_label = tk.Label(self.root, text="")
        self.result_label.grid(row=3, column=0, columnspan=2)

        self.calculate_button = tk.Button(self.root, text="Calcular ruta", command=self.calculate_route2)
        self.calculate_button.grid(row=4, column=0, columnspan=2)

        self.calculate_butto = tk.Button(self.root, text="Mostrar grafo", command=self.crearGrafo)
        self.calculate_butto.grid(row=7, column=1, columnspan=2)
        
        # self.min_stops_button = tk.Button(self.root, text="Calcular ruta con mínimas paradas", command=self.calculate_min_stops_route)
        # self.min_stops_button.grid(row=5, column=0, columnspan=2)

        # self.min_stops_result_label = tk.Label(self.root, text="")
        # self.min_stops_result_label.grid(row=6, column=0, columnspan=2)
        
    def run(self):
        self.root.mainloop()

    def calculate_route(self):
        origin = self.origin_entry.get().strip().upper()
        destination = self.destination_entry.get().strip().upper()
        has_visa = self.visa_var.get()

        if origin not in self.airport_codes or destination not in self.airport_codes:
            self.result_label.config(text="Origen o destino no válido.")
            return

        src_idx = self.airport_codes.index(origin)
        dest_idx = self.airport_codes.index(destination)

        cost, path = self.graph.find_route(src_idx, dest_idx, has_visa)
        if cost == float('inf'):
            self.result_label.config(text="No se encontró una ruta válida.")
        else:
            path = [self.airport_codes[i] for i in path]
            self.result_label.config(text=f"Ruta: {' -> '.join(path)}\nCosto: ${cost}")

    def crearGrafo(self):
        G=nx.DiGraph()
        for e in self.edges:
            agregar_arista(G,e[0],e[1],e[2])
        
        pos = nx.layout.planar_layout(G)
        nx.draw_networkx(G, pos)
        labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
        plt.title("Grafo con NetworkX")
        plt.show()
    

    def calculate_route2(self):
        origin = self.origin_entry.get().strip().upper()
        destination = self.destination_entry.get().strip().upper()
        has_visa = self.visa_var.get()

        if origin not in self.airport_codes or destination not in self.airport_codes:
            self.result_label.config(text="Origen o destino no válido.")
            return

        src_idx = self.airport_codes.index(origin)
        dest_idx = self.airport_codes.index(destination)

        cost, path = self.graph.find_route(src_idx, dest_idx, has_visa)
        stops, path_stops = self.graph.find_route(src_idx, dest_idx, has_visa, minimize_cost=False)

        if cost == float('inf') or stops == float('inf'):
            self.result_label.config(text="No se encontró una ruta válida.")
        else:
            path = [self.airport_codes[i] for i in path]
            path_stops = [self.airport_codes[i] for i in path_stops]
            self.result_label.config(text=f"Ruta más barata: {' -> '.join(path)}\nCosto: ${cost}\n\nRuta con menos paradas: {' -> '.join(path_stops)}\nParadas: {stops}")
    
    # def calculate_min_stops_route(self):
    #     origin = self.origin_entry.get().upper()
    #     destination = self.destination_entry.get().upper()

    #     src_idx = self.airport_codes.index(origin)
    #     dest_idx = self.airport_codes.index(destination)

    #     stops, path = self.graph.find_min_stops_route(src_idx, dest_idx)

    #     if stops == float('inf'):
    #         self.min_stops_result_label.config(text="No se encontró una ruta válida.")
    #         print(stops)
    #         print(path)
    #     else:
    #         self.min_stops_result_label.config(text=f"La ruta con las mínimas paradas es: {path} con {stops} paradas.")
    #         print(stops)
    #         print(path)