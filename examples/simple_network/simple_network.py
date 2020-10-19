import time
from distsim import Network
import pathlib
from multiprocessing import current_process


def node_code():
    # get current node object
    node = current_process()
    logger = node.get_logger()

    logger.info(f"Starting node.")

    for node_name in node.out_pipes.keys():
        node.send_to(node_name, f"Msg from node {node.name}")

    for node_name in node.in_pipes:
        msg = node.recv_from(node_name)
        logger.info(f"Recieved msg: {msg}")

    time.sleep(2)

    logger.info(f"Shutting down.")


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

if __name__ == "__main__":
    network = Network(NETWORK_ARCHITECTURE,
                      log_dir=pathlib.Path(__file__).parent.absolute())

    network.start()
    network.join()
