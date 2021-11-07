import typing
import pathlib
import logging
import random

from multiprocessing import Process


class Node(Process):
    def __init__(
        self,
        name: str,
        function: typing.Callable,
        args: typing.Collection = [],
        log_dir: pathlib.Path = pathlib.Path.cwd(),
    ) -> None:
        super().__init__(name=name, target=function, args=tuple(args))

        self.connections = {}
        self.log_dir = log_dir

    @property
    def neighbors(self) -> typing.Tuple:
        return tuple(self.connections.keys())

    def init_logger(self) -> logging.Logger:
        logger = logging.getLogger(self.name)
        hdlr = logging.FileHandler(self.log_dir.joinpath(f"{self.name}.log"), mode="w")

        formatter = logging.Formatter(
            f"%(asctime)s %(levelname)s {self.name}: %(message)s"
        )

        hdlr.setFormatter(formatter)
        logger.addHandler(hdlr)
        logger.setLevel(logging.INFO)
        
        return logger

    def recv_from(self, name) -> object:
        connection = self.connections[name]
        return connection.recv(), name
    
    def recv_any(self, blocking=True) -> object:
        while True:
            neighbors_with_msg = [name for name, conn in self.connections.items() if conn.poll()]

            if not blocking or neighbors_with_msg:
                break

        return self.recv_from(random.choice(neighbors_with_msg))

    def send_to(self, name, msg) -> None:
        connections = self.connections[name]
        connections.send(msg)
