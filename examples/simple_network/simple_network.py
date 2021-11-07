import time

from multiprocessing import current_process

from distsim import Network, NodeDefinition


def node_code():
    # get current node object
    node = current_process()

    # get logger
    logger = node.init_logger()

    logger.info(f"Starting node.")

    # send msg to each neighbors
    for node_name in node.neighbors:
        msg = f"Msg from node {node.name}"
        node.send_to(node_name, msg)
        logger.info(f"Sent {msg} to {node_name}.")

    # recieve msg from each input pipelines
    for node_name in node.neighbors:
        msg, _ = node.recv_from(node_name)
        logger.info(f"Recv {msg} from {node_name}.")

    time.sleep(2)

    logger.info(f"Shutting down.")

# run network
if __name__ == "__main__":
    network_topology = (
        NodeDefinition("node1", node_code, connections=["node2"]),
        NodeDefinition("node2", node_code, connections=["node1"]),
    )

    network = Network(network_topology)

    network.start()
    network.join()
