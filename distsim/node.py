import multiprocessing
import random
from multiprocessing import Process
import logging
import os


class Node(Process):
    """Represents one node in the distributed network"""

    def __init__(self, name, function, arguments, log_dir):
        if not callable(function):
            raise ValueError(
                f"{name} node function must be a callable not a {type(function)}")

        if type(arguments) is not tuple:
            raise ValueError(
                f"{name} node args must be a tuple not a {type(arguments)}.")

        super().__init__(name=name, target=function, args=arguments)

        self.in_pipes = {}
        self.out_pipes = {}
        self.log_dir = log_dir

    def get_logger(self):
        logger = logging.getLogger(self.name)
        hdlr = logging.FileHandler(
            os.path.join(self.log_dir, f'{self.name}.log'), mode='w')
        formatter = logging.Formatter(
            f'%(asctime)s %(levelname)s {self.name}: %(message)s')
        hdlr.setFormatter(formatter)
        logger.addHandler(hdlr)
        logger.setLevel(logging.INFO)

        return logger

    def add_in_pipe(self, node_id, pipe):
        self.in_pipes[node_id] = pipe

    def add_out_pipe(self, node_id, pipe):
        self.out_pipes[node_id] = pipe

    def recv_any(self, timeout=0, blocking=True):
        connections_with_msg = []

        wait_for_message = True

        while wait_for_message:
            for name, connection in self.in_pipes.items():
                if connection.poll(timeout):
                    wait_for_message = False
                    connections_with_msg.append((name, connection))

            if not blocking:
                wait_for_message = False

        if connections_with_msg:
            name, chosen_connection = random.choice(connections_with_msg)
            return chosen_connection.recv(), name
        else:
            return None, None

    def poll_from(self, name, timeout):
        """
        If timeout is not specified then it will return immediately. If timeout is a number then this specifies the maximum time in seconds to block. If timeout is None then an infinite timeout is used.
        """
        connection = self.in_pipes[name]

        return connection.poll(timeout)

    def recv_from(self, name):
        connection = self.in_pipes[name]

        return connection.recv()

    def send_to(self, name, msg):
        connection = self.out_pipes[name]

        return connection.send(msg)
