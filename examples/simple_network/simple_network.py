import time
import pathlib
from multiprocessing import current_process

from distsim import Network


def node_code():
    # get current node object
    node = current_process()

    # get logger
    logger = node.get_logger()

    logger.info(f"Starting node.")

    # send msg to each output pipelines
    for node_name in node.out_pipes.keys():
        node.send_to(node_name, f"Msg from node {node.name}")

    # recieve msg from each input pipelines
    for node_name in node.in_pipes:
        msg = node.recv_from(node_name)
        logger.info(f"Recieved msg: {msg}")

    time.sleep(2)

    logger.info(f"Shutting down.")


# define network architecture
NETWORK_ARCHITECTURE = {
    'node1': {
        'out': {'node2', },
        'function': node_code,
        'args': ()},
    'node2': {
        'out': {'node1', },
        'function': node_code,
        'args': ()},
}

# run network
if __name__ == "__main__":
    network = Network(NETWORK_ARCHITECTURE,
                      log_dir=pathlib.Path(__file__).parent.absolute())

    network.start()
    network.join()
