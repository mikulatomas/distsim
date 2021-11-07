import typing
import pathlib

from multiprocessing import Pipe

import distsim

from .node import Node


class Network:
    def __init__(
        self, topology: typing.Collection["distsim.NodeDefinition"], log_dir: pathlib.Path = pathlib.Path.cwd()
    ) -> None:
        self.nodes = {}

        for node_definition in topology:
            node = Node.from_definition(node_definition, log_dir)
            self.nodes[node.name] = node

        for node_definition in topology:
            for neighbor in node_definition.connections:
                if neighbor not in self.nodes.keys():
                    raise ValueError(
                        f"The {neighbor} is not present in given network topology."
                    )

                conn1, conn2 = Pipe()

                self.nodes[node_definition.name].connections[neighbor] = conn1
                self.nodes[neighbor].connections[node_definition.name] = conn2

    def __repr__(self):
        return f"{self.__class__.__name__}(nodes={len(self.nodes)})"

    def __str__(self):
        return self.__repr__

    def start(self):
        """Starts all nodes in the network"""
        for node in self.nodes.values():
            node.start()

    def terminate(self):
        """Terminate all nodes in the network"""
        for node in self.nodes.values():
            node.terminate()

    def kill(self):
        """Kill all nodes in the network"""
        for node in self.nodes.values():
            node.kill()

    def join(self):
        """Join all nodes in the network"""
        for node in self.nodes.values():
            node.join()
