import time
import pathlib
import threading
from multiprocessing import current_process

from distsim import Network


def node_code():
    # get current node object
    node = current_process()

    # get logger
    logger = node.get_logger()

    logger.info(f"Starting node.")

    def outputs(node, logger):
        for node_name in node.out_pipes.keys():
            logger.info(f"Sending msg: Msg from node {node.name}")
            node.send_to(node_name, f"Msg from node {node.name}")

    def inputs(node, logger):
        for node_name in node.in_pipes:
            msg = node.recv_from(node_name)
            logger.info(f"Recieved msg: {msg}")

    out_msg = threading.Thread(target=outputs, args=(node, logger))
    in_msg = threading.Thread(target=inputs, args=(node, logger))

    out_msg.start()
    in_msg.start()

    out_msg.join()
    in_msg.join()

    logger.info(f"Shutting down.")


# define network architecture
NETWORK_ARCHITECTURE = {}
number_of_nodes = 10

for i in range(number_of_nodes):
    # generate output pipes
    out = []
    for j in range(number_of_nodes):
        if i != j:
            out.append(f"node{j}")

    NETWORK_ARCHITECTURE[f"node{i}"] = {
        'out': set(out),
        'function': node_code,
        'args': ()
    }

# run network
if __name__ == "__main__":
    network = Network(NETWORK_ARCHITECTURE,
                      log_dir=pathlib.Path(__file__).parent.absolute())

    network.start()
    network.join()
