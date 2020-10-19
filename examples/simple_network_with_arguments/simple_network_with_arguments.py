import time
import pathlib
from multiprocessing import current_process

from distsim import Network


def node_code(arg):
    # get current node object
    node = current_process()

    # get logger
    logger = node.get_logger()

    logger.info(f"Starting node.")

    logger.info(f"Argument is: {arg}")

    logger.info(f"Shutting down.")


# define network architecture
NETWORK_ARCHITECTURE = {
    'node1': {
        'out': {'node2', },
        'function': node_code,
        'args': ('argument for node 1', )},
    'node2': {
        'out': {'node1', },
        'function': node_code,
        'args': ('argument for node 2', )},
}

# run network
if __name__ == "__main__":
    network = Network(NETWORK_ARCHITECTURE,
                      log_dir=pathlib.Path(__file__).parent.absolute())

    network.start()
    network.join()
