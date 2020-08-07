import multiprocessing
import random
from multiprocessing import Process


class Node(Process):
    """Represents one node in the distributed network"""

    def __init__(self, name, function, arguments):
        if not callable(function):
            raise ValueError(
                f"{name} node function must be a callable not a {type(function)}")

        if type(arguments) is not tuple:
            raise ValueError(
                f"{name} node args must be a tuple not a {type(arguments)}.")

        Process.__init__(self, name=name, target=function, args=arguments)

        self.in_pipes = {}
        self.out_pipes = {}

    def _add_pipe(self, pipe_type, node_id, pipe):
        pipes = pipe_type.get(node_id)

        if pipes is None:
            pipe_type[node_id] = [pipe]
        else:
            pipe_type[node_id].append(pipe)

    def add_in_pipe(self, node_id, pipe):
        self._add_pipe(self.in_pipes, node_id, pipe)

    def add_out_pipe(self, node_id, pipe):
        self._add_pipe(self.out_pipes, node_id, pipe)

    def recv_any(self, timeout=0):
        connections_with_msg = []

        recieved = False

        while not recieved:
            for name, pipes in self.in_pipes.items():
                for connection in pipes:
                    if connection.poll(timeout):
                        recieved = True
                        connections_with_msg.append((name, connection))

        name, chosen_connection = random.choice(connections_with_msg)

        return chosen_connection.recv(), name

    def recv_from(self, name):
        connection = self.in_pipes[name][0]

        return connection.recv()

    def send_to(self, name, msg):
        connection = self.out_pipes[name][0]

        return connection.send(msg)
