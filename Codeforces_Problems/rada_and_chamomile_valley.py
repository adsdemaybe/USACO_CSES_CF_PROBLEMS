class Connection:
    """Represents a connection/edge with a destination and order number"""
    def __init__(self, to_node, connection_number):
        self.to = to_node  # The destination node
        self.number = connection_number  # Order in which this connection was added
    
    def __str__(self):
        return f"Connection #{self.number} -> House {self.to.id}"


class Node:
    def __init__(self, house_id):
        self.id = house_id
        self.connections = []  # List of Connection objects
    
    def add_connection(self, to_node, connection_number):
        """Add a connection to another node with a connection number"""
        connection = Connection(to_node, connection_number)
        self.connections.append(connection)
    
    def get_connection_to(self, house_id):
        """Get the connection object that leads to a specific house"""
        for conn in self.connections:
            if conn.to.id == house_id:
                return conn
        return None


def solve():
    # Read number of test cases
    # t = int(input())
    t = 1  # For testing purposes, set to 1
    
    for _ in range(t):
        # Read n (houses) and m (lanes)
        n, m = map(int, input().split())
        
        # Create nodes for each house
        houses = {}
        for i in range(1, n + 1):
            houses[i] = Node(i)
        
        # Read lanes and create bidirectional connections
        for i in range(m):
            u, v = map(int, input().split())
            connection_number = i + 1  # Number connections starting from 1
            
            # Add bidirectional connections with the same connection number
            houses[u].add_connection(houses[v], connection_number)
            houses[v].add_connection(houses[u], connection_number)
        
        # Print connections (for debugging)
        for house_id in range(1, n + 1):
            node = houses[house_id]
            print(f"House {node.id}:")
            for conn in node.connections:
                print(f"  {conn}")
        print()  # Empty line between test cases

if __name__ == "__main__":
    solve()