import time

from multiprocessing import current_process

from distsim import Network, NodeDefinition


def spammer_code():
    # get current node object
    node = current_process()

    # get logger
    logger = node.init_logger()

    logger.info(f"Starting node.")

    for i in range(2):
        logger.info(f"Spamming victim.")
        time.sleep(1)
        node.send_to("victim", f'SPAM from {node.name}!')

    logger.info(f"Shutting down.")


def victim_code():
    node = current_process()

    logger = node.init_logger()

    logger.info(f"Starting node.")

    for _ in range(8):
        logger.info(node.recv_any())

    logger.info(f"Shutting down.")

if __name__ == "__main__":
    spammers = [NodeDefinition(f"spammer{idx}", spammer_code, connections=["victim"]) for idx in range(4)]
    victim = [NodeDefinition("victim", victim_code)]

    network = Network(spammers + victim)

    network.start()
    network.join()
