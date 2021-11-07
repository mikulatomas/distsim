from multiprocessing import current_process

from distsim import Network, NodeDefinition


def node_code(arg):
    # get current node object
    node = current_process()

    # init logger
    logger = node.init_logger()

    logger.info(f"Starting node.")

    logger.info(f"Argument is: {arg}")

    logger.info(f"Shutting down.")


if __name__ == "__main__":
    network_topology = (
        NodeDefinition("node1", node_code, args=(1,), connections=["node2"]),
        NodeDefinition("node2", node_code, args=(2,), connections=["node1"]),
    )

    network = Network(network_topology)

    network.start()
    network.join()

