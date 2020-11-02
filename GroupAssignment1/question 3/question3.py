import networkx as nx
import matplotlib.pyplot as plt
from classes.bfs import BfsTraverser
G = nx.Graph()
nodes=["Sports","Siwaka","Ph1A","Ph1B","STC","Ph2","Ph3","J1","Mada","ParkingLot"]
G.add_nodes_from(nodes)
G.nodes()#confirm nodes
#Add Edges and their weights
G.add_edge("Sports","Siwaka",weight="450")
G.add_edge("Siwaka","Ph1A",weight="10")
G.add_edge("Siwaka","Ph1B",weight="230")
G.add_edge("Ph1A","Ph1B",weight="100")
G.add_edge("Ph1B","STC",weight="50")
G.add_edge("Ph1B","Ph2",weight="112")
G.add_edge("Ph2","Ph3",weight="500")
G.add_edge("Ph2","J1",weight="600")
G.add_edge("Ph3","ParkingLot",weight="350")
G.add_edge("STC","ParkingLot",weight="250")
G.add_edge("STC","Ph2",weight="50")
G.add_edge("Ph1A","Mada",weight="850")
G.add_edge("J1","Mada",weight="200")
G.add_edge("Mada","ParkingLot",weight="700")
#position the nodes to resemble Nairobis map
G.nodes["STC"]['pos']=(0,0)
G.nodes["Ph1B"]['pos']=(0,2)
G.nodes["Ph1A"]['pos']=(0,4)
G.nodes["Siwaka"]['pos']=(-1,4)
G.nodes["Sports"]['pos']=(-2,4)
G.nodes["Ph2"]['pos']=(1,2)
G.nodes["J1"]['pos']=(2,2)
G.nodes["Ph3"]['pos']=(2,0)
G.nodes["ParkingLot"]['pos']=(2,-2)
G.nodes["Mada"]['pos']=(3,2)
#store all positions in a variable
node_pos = nx.get_node_attributes(G,'pos')
#call BFS to return set of all possible routes to the goal
route_bfs = BfsTraverser()
routes = route_bfs.BFS(G,"Sports","ParkingLot")
print(route_bfs.visited)
route_list = route_bfs.visited
#color the nodes in the route_bfs
node_col = ['darkturquoise' if not node in route_list else 'peru' for node in G.nodes()]
peru_colored_edges = list(zip(route_list,route_list[1:]))
#color the edges as well
#print(peru_colored_edges)
edge_col = ['darkturquoise' if not edge in peru_colored_edges else 'peru' for edge in G.edges()]
arc_weight=nx.get_edge_attributes(G,'weight')
nx.draw_networkx(G, node_pos,node_color= node_col, node_size=450)
nx.draw_networkx_edges(G, node_pos,width=2,edge_color= edge_col)
#nx.draw_networkx_edge_labels(G, node_pos,edge_color= edge_col, edge_labels=arc_weight)

nx.draw_networkx_edge_labels(G, node_pos, edge_labels=arc_weight)
plt.axis('off')
plt.show()
