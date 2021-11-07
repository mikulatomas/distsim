from multiprocessing import current_process

from distsim import Network, Node


def node_code(arg):
    node = current_process()

    logger = node.init_logger()

    logger.info(f"Starting node.")

    logger.info(f"Argument is: {arg}")

    logger.info(f"Shutting down.")


if __name__ == "__main__":
    nodes = (
        Node("node1", node_code, args=(1,)),
        Node("node2", node_code, args=(2,)),
    )

    network = Network(nodes)

    network.start()
    network.join()

