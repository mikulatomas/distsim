from multiprocessing import Pipe

from .node import Node


class Network():
    """Represents distributed network"""

    METADATA = ['out', 'function', 'args']

    def __init__(self, network_architecture, log_dir):
        if type(network_architecture) is not dict:
            raise ValueError(
                f"Network architecture must be a dict not a {type(network_architecture)}.")

        # Small waste of performance
        for node_name, metadata in network_architecture.items():
            if set(metadata.keys()) != set(self.METADATA):
                raise ValueError(
                    f"Node {node_name} in the network architecture must include 'out', 'function' and 'args' values.")

        # Build Nodes
        self.nodes = dict(((name, Node(name, network_architecture[name]['function'], network_architecture[name]['args'], log_dir))
                           for name in network_architecture.keys()))

        # Build Pipes
        for source_node, metadata in network_architecture.items():
            if type(metadata['out']) is not set:
                raise ValueError(
                    f"{source_node} node 'out' metadata must be a set not a {type(metadata['out'])}")

            for target_node in metadata['out']:
                if target_node not in network_architecture.keys():
                    raise ValueError(
                        f"Target node {target_node} does not exists.")

                in_pipe, out_pipe = Pipe(duplex=False)
                self.nodes[source_node].add_out_pipe(target_node, out_pipe)
                self.nodes[target_node].add_in_pipe(source_node, in_pipe)

    def start(self):
        """Starts all nodes in the network"""
        for name, node in self.nodes.items():
            node.start()

    def terminate(self):
        """Terminate all nodes in the network"""
        for node, node in self.nodes.items():
            node.terminate()

    def kill(self):
        """Kill all nodes in the network"""
        for node, node in self.nodes.items():
            node.kill()

    def join(self):
        """Join all nodes in the network"""
        for node, node in self.nodes.items():
            node.join()
