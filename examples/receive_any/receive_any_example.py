import time

from multiprocessing import current_process

from distsim import Network, Node, Link, Message


def spammer_code():
    node = current_process()

    logger = node.init_logger()

    logger.info(f"Starting node.")

    for i in range(2):
        time.sleep(1)
        msg = Message("hidden", f"SPAM from {node.name}!")
        logger.info(f"Sent {msg}")
        node.send_to("victim", msg)

    logger.info(f"Shutting down.")


def victim_code():
    node = current_process()

    logger = node.init_logger()

    logger.info(f"Starting node.")

    for _ in range(8):
        logger.info(node.recv_any())

    logger.info(f"Shutting down.")

if __name__ == "__main__":
    spammers = [Node(f"spammer{idx}", spammer_code) for idx in range(4)]
    victim = [Node("victim", victim_code)]

    links = [Link(f"spammer{idx}", "victim") for idx in range(4)]

    network = Network(spammers + victim, links)

    network.start()
    network.join()
