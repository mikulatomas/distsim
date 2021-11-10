import time

from multiprocessing import current_process

from distsim import Network, Node, Link, Message


def node_code():
    node = current_process()

    logger = node.init_logger()

    logger.info(f"Starting node.")

    for node_name in node.neighbors:
        msg = Message(node.name, f"Msg from node {node.name}")
        node.send_to(node_name, msg)
        logger.info(f"Sent {msg}.")

    for node_name in node.neighbors:
        msg = node.recv_from(node_name)
        logger.info(f"Recv {msg}.")

    time.sleep(2)

    logger.info(f"Shutting down.")


if __name__ == "__main__":
    nodes = (
        Node("node1", node_code),
        Node("node2", node_code)
        )
    
    links = (
        Link("node1", "node2"),
    )

    network = Network(nodes, links)

    network.start()
    network.join()
