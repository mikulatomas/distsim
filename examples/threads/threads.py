import threading

from multiprocessing import current_process

from distsim import Network, Node, Link


def node_code():
    node = current_process()

    logger = node.init_logger()

    logger.info(f"Starting node.")

    def outputs(node, logger):
        for node_name in node.neighbors:
            logger.info(f"Sending msg: Msg from node {node.name}")
            node.send_to(node_name, f"Msg from node {node.name}")

    def inputs(node, logger):
        for node_name in node.neighbors:
            msg, _ = node.recv_from(node_name)
            logger.info(f"Recieved msg: {msg}")

    out_msg = threading.Thread(target=outputs, args=(node, logger))
    in_msg = threading.Thread(target=inputs, args=(node, logger))

    out_msg.start()
    in_msg.start()

    out_msg.join()
    in_msg.join()

    logger.info(f"Shutting down.")


if __name__ == "__main__":
    number_of_nodes = 10

    nodes = [Node(f"node{idx}", node_code) for idx in range(number_of_nodes)]
    # each node will have link to each other node
    links = [Link(f"node{i}", f"node{j}") for j in range(number_of_nodes) for i in range(number_of_nodes) if i != j]

    network = Network(nodes, links)

    network.start()
    network.join()
