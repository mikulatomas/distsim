import typing
import pathlib
import logging
import random

from multiprocessing import Process

import distsim


class Node(Process):
    def __init__(
        self,
        name: str,
        function: typing.Callable,
        args: typing.Collection = [],
        log_dir: pathlib.Path = pathlib.Path.cwd(),
    ) -> None:
        """Represents node of distributed network. Formally based on multiprocessing.Process.

        Args:
            name (str): unique identifier
            function (typing.Callable): function which is executed by the node
            args (typing.Collection, optional): arguments for the function. Defaults to [].
            log_dir (pathlib.Path, optional): root directory for logs. Defaults to pathlib.Path.cwd().
        """
        super().__init__(name=name, target=function, args=tuple(args))

        self.connections = {}
        self.log_dir = log_dir

    @property
    def neighbors(self) -> typing.Tuple[str,]:
        """Names of neighbor nodes.

        Returns:
            typing.Tuple[str,]: names of nodes
        """
        return tuple(self.connections.keys())

    def init_logger(self) -> logging.Logger:
        """Initialize logger. Should be called only once in the given function.

        Returns:
            logging.Logger: logger
        """
        logger = logging.getLogger(self.name)
        hdlr = logging.FileHandler(self.log_dir.joinpath(f"{self.name}.log"), mode="w")

        formatter = logging.Formatter(
            f"%(asctime)s %(levelname)s {self.name}: %(message)s"
        )

        hdlr.setFormatter(formatter)
        logger.addHandler(hdlr)
        logger.setLevel(logging.INFO)
        
        return logger

    def recv_from(self, name) -> 'distsim.Message':
        """Receive a message from neighbor with given name.

        Blocking till message is received.

        Args:
            name ([type]): name of the neighbor

        Returns:
            typing.Tuple[object, str]: message and name of the node
        """
        connection = self.connections[name]
        return connection.recv()
    
    def recv_any(self, blocking: bool = True) -> typing.Optional['distsim.Message']:
        """Receive first avaliable message from neighbors.

        Args:
            blocking (bool, optional): If True, waits till some message is avaliable. Defaults to True.

        Returns:
            typing.Tuple[object, str]: message and name of the node
        """
        while True:
            neighbors_with_msg = [name for name, conn in self.connections.items() if conn.poll()]

            if not blocking or neighbors_with_msg:
                break

        try:
            return self.recv_from(random.choice(neighbors_with_msg))
        except IndexError:
            return None

    def send_to(self, name: str, msg: 'distsim.Message') -> None:
        """Send message to neighbor with given name.

        Args:
            name (str): name of the neighbor
            msg (distsim.Message): message
        """
        connections = self.connections[name]
        connections.send(msg)
