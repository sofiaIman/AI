from collections import defaultdict 
from frontier import PriorityQueue

class UcsTraverser:
        # Constructor 
        def __init__(self): 
            self.visited = []
            self.end_search = False

        def ed(self, graph):
            print("test edge data:", graph.get_edge_data("sports", "siwaka")["weight"])

        def ucs(self,graph, start_node, goal_node):
            frontier = PriorityQueue()

            #root goal test
            if start_node is goal_node:
                print("goal", start_node, "reached at cost 0")
                self.end_search = True

            #set of visited nodes
            self.visited.append(start_node)

            #fill frontier
            for i in list(graph[start_node]):
                frontier.insert((i, graph.get_edge_data(start_node, i)["weight"]), graph.get_edge_data(start_node, i)["weight"])
                        

            while not frontier.is_empty() and not self.end_search: 
                # Dequeue a vertex from 
                    current_node, cost_node = frontier.remove()
                    if current_node not in self.visited:
                            self.visited.append(current_node)
                            print("Walk to ", current_node, end = "\n")
                            print(cost_node)

                            if current_node is goal_node:
                                print("goal",current_node , "reached at cost", cost_node)
                                self.end_search = True

                            # Get all adjacent vertices of the
                            # dequeued vertex s. If a adjacent
                            # has not been visited, then mark it
                            # visited and enqueue it

                            for i in list(graph[current_node]):
                                if i not in self.visited:
                                        cumulative_cost = int(graph.get_edge_data(current_node, i)["weight"]) + int(cost_node)
                                        frontier.insert((i, cumulative_cost), cumulative_cost)
