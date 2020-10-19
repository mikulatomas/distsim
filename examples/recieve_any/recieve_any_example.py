import time
import pathlib
from multiprocessing import current_process

from distsim import Network


def spammer_code():
    # get current node object
    node = current_process()

    # get logger
    logger = node.get_logger()

    logger.info(f"Starting node.")

    for i in range(20):
        logger.info(f"Spamming victim.")
        node.send_to('victim', f'SPAM from {node.name}!')

    logger.info(f"Shutting down.")


def victim_code():
    # get current node object
    node = current_process()

    # get logger
    logger = node.get_logger()

    logger.info(f"Starting node.")

    logger.info(node.recv_any())

    logger.info(f"Shutting down.")


# define network architecture
NETWORK_ARCHITECTURE = {
    'spammer1': {
        'out': {'victim', },
        'function': spammer_code,
        'args': ()},
    'spammer2': {
        'out': {'victim', },
        'function': spammer_code,
        'args': ()},
    'spammer3': {
        'out': {'victim', },
        'function': spammer_code,
        'args': ()},
    'victim': {
        'out': None,
        'function': victim_code,
        'args': ()},
}

# run network
if __name__ == "__main__":
    network = Network(NETWORK_ARCHITECTURE,
                      log_dir=pathlib.Path(__file__).parent.absolute())

    network.start()
    network.join()
