# Gabriele Fronzoni 
# matricola: 0001068902

class Node: 
    """
    A class that represent a network node.
    Each node has a Routing Table that stores, for each node, distances and next hop
    for each node.
    
    Attributes:
        name : str
            Name of the node.
        routingTable : dict
            A dictionary where keys are names of other nodes and values are pair of distance and 
            name of the next hop.
    
    """
    def __init__(self, name):
        """
        Initialize a node with its name and an initial routing table containing itself.
        
        Args:
            name : str
                The name of the node.
        """
        self.name = name
        self.routingTable = {name : (0, name) }
        
    def updateTable(self, neighbors):
        """
        Updates the routing table of the current node based on information from its neighbors.

        Args:
            neighbors : dict
            A dictionary of neighboring nodes and the weights of the links to them.
            Keys are Node objects (neighbors), and values are the weights (int).
        """
        for neighbor, weight in neighbors.items():
            for node, infos in neighbor.routingTable.items():
                if node not in self.routingTable: #node is not present in node's routing table
                    self.routingTable.update({node: (weight+infos[0], neighbor.name)})
                elif weight+infos[0] < self.routingTable.get(node)[0]: #check if the path through the neighbour costs less
                    self.routingTable.update({node: (weight+infos[0], neighbor.name)})
                    
    def printRoutingTable(self):
        """
        Print the routing table of the node.
        Print for each reachable node distance and next hop name. 
        """
        for node, (distance, hop) in self.routingTable.items():
            print("Node - " + node + " Distance - " + str(distance) + " Next Hop - " + hop)
                    
if __name__ == "__main__":
    """
    Simulate a network and creation and filling of routing table of each node.
    """
    # Nodes of the network.
    nodes = {
        "A" : Node("A"),
        "B" : Node("B"),
        "C" : Node("C"),
        "D" : Node("D"),
        "E" : Node("E"),
        "F" : Node("F"),
        "G" : Node("G")
    }
    
    # Neighbors for each node and weight of each link.
    network = {
        "A" : {nodes.get("B"): 2, nodes.get("C"):5},
        "B" : {nodes.get("C"): 2, nodes.get("A"):2 },
        "C" : {nodes.get("A"): 5, nodes.get("B"):2, nodes.get("D"):4, nodes.get("E"):6 },
        "D" : {nodes.get("C"): 4, nodes.get("B"):8, nodes.get("F"):4, nodes.get("E"):3 },
        "E" : {nodes.get("C"): 6, nodes.get("D"):3, nodes.get("G"):8},
        "F" : {nodes.get("D"): 4, nodes.get("G"):5 },
        "G" : {nodes.get("E"): 8, nodes.get("F"):5 },
    }
    
    # Iterate the exchange of routing table between nodes for number of nodes time to 
    # reach convergence. 
    for iteration in range(len(nodes)):
        for name, node in nodes.items(): 
            print("Routing table of node " + name + " at iteration n." + str(iteration+1))
            node.updateTable(network.get(node.name))
            node.printRoutingTable()
    
    