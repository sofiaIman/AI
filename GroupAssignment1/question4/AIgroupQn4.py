import networkx as nx
import matplotlib.pyplot as plt
from qn4 import UcsTraverser
from collections import defaultdict 


G = nx.Graph()
nodes=["sports","siwaka","ph1A","ph1B","STC","ph2","ph3","J1","mada","parkinglot"]
G.add_nodes_from(nodes)
G.nodes()#confirm nodes

#Add Edges and their weights
G.add_edge("sports","siwaka",weight="450")
G.add_edge("siwaka","ph1A",weight="10")
G.add_edge("siwaka","ph1B",weight="230")
G.add_edge("ph1A","ph1B",weight="100")
G.add_edge("ph1B","STC",weight="50")
G.add_edge("ph1B","ph2",weight="112")
G.add_edge("ph2","ph3",weight="500")
G.add_edge("ph2","J1",weight="600")
G.add_edge("ph3","parkinglot",weight="350")
G.add_edge("STC","parkinglot",weight="250")
G.add_edge("STC","ph2",weight="50")
G.add_edge("ph1A","mada",weight="850")
G.add_edge("J1","mada",weight="200")
G.add_edge("mada","parkinglot",weight="700")

#position the nodes to resemble Madaraka Estate Network
G.nodes["STC"]['pos']=(0,0)
G.nodes["ph1B"]['pos']=(0,2)
G.nodes["ph1A"]['pos']=(0,4)
G.nodes["siwaka"]['pos']=(-1,4)
G.nodes["sports"]['pos']=(-2,4)
G.nodes["ph2"]['pos']=(1,2)
G.nodes["J1"]['pos']=(2,2)
G.nodes["ph3"]['pos']=(2,0)
G.nodes["parkinglot"]['pos']=(2,-2)
G.nodes["mada"]['pos']=(3,2)
#store all positions in a variable
node_pos = nx.get_node_attributes(G,'pos')

#ucs  tr
route_ucs = UcsTraverser()
route_ucs.ucs(G, "sports", "parkinglot")

print("Visited:", route_ucs.visited)
route_list = route_ucs.visited

#color the nodes in the route_ucs
node_col = ['darkturquoise' if not node in route_list else 'peru' for node in G.nodes()]
peru_colored_edges = list(zip(route_list,route_list[1:]))

#color the edges as well
#print(peru_colored_edges)
edge_col = ['darkturquoise' if not edge in peru_colored_edges else 'peru' for edge in G.edges()]

arc_weight=nx.get_edge_attributes(G,'weight')
nx.draw_networkx(G, node_pos,node_color = node_col, node_size=500)
nx.draw_networkx_edges(G, node_pos,width=2, edge_color=edge_col)
#nx.draw_networkx_edge_labels(G, node_pos,edge_color= edge_col, edge_labels=arc_weight)

nx.draw_networkx_edge_labels(G, node_pos, edge_labels=arc_weight)
plt.axis('off')
#print(nx.info(G))
plt.show()


