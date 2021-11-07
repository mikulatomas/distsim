import typing
import pathlib

from multiprocessing import Pipe

import distsim

from .node import Node


class Network:
    def __init__(
        self,
        nodes: typing.Collection["distsim.Node"],
        links: typing.Collection["distsim.Link"] = [],
        log_dir: pathlib.Path = pathlib.Path.cwd()
    ) -> None:
        self.nodes = dict(((node.name, node) for node in nodes))

        for node in self.nodes.values():
            node.log_dir = log_dir

        # print(links)
        for node1, node2 in links:
            if node1 not in self.nodes or node2 not in self.nodes:
                raise ValueError(
                        f"One of the two ends of given link ({node1, node2}) is not valid name of network node."
                    )

            conn1, conn2 = Pipe()

            self.nodes[node1].connections[node2] = conn1
            self.nodes[node2].connections[node1] = conn2

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
