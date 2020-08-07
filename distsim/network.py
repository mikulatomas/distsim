from multiprocessing import Pipe

from .node import Node


class Network():
    """Represents distributed network"""

    METADATA = ['out', 'function', 'args']

    def __init__(self, network_architecture):
        if type(network_architecture) is not dict:
            raise ValueError(
                f"Network architecture must be a dict not a {type(network_architecture)}.")

        # Build Nodes
        self.nodes = dict(((name, Node(name, network_architecture[name]['function'], network_architecture[name]['args']))
                           for name in network_architecture.keys()))

        # Build Pipes
        for source_node, metadata in network_architecture.items():
            if set(metadata.keys()) != set(self.METADATA):
                raise ValueError(
                    f"Node {source_node} in the network architecture must include 'out', 'function' and 'args' values.")

            if type(metadata['out']) is not tuple:
                raise ValueError(
                    f"{source_node} node 'out' metadata must be a tuple not a {type(metadata['out'])}")

            for target_node in metadata['out']:
                if target_node not in network_architecture.keys():
                    raise ValueError(
                        f"Target node {target_node} does not exists.")

                in_pipe, out_pipe = Pipe(duplex=False)
                self.nodes[source_node].add_out_pipe(target_node, out_pipe)
                self.nodes[target_node].add_in_pipe(source_node, in_pipe)

    def start(self):
        """Starts all nodes in the network"""
        for node in self.nodes:
            node.start()

    def terminate(self):
        """Terminate all nodes in the network"""
        for node in self.nodes:
            node.terminate()

    def kill(self):
        """Kill all nodes in the network"""
        for node in self.nodes:
            node.kill()

    def join(self):
        """Join all nodes in the network"""
        for node in self.nodes:
            node.join()
