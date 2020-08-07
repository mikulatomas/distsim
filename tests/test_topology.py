# import pytest
# from distsim import Network


# def test_basic_topology():

#     NETWORK_ARCHITECTURE = {
#         'node1': {
#             'out': ('node2', 'node3'),
#             'function': (lambda x: x),
#             'args': (1,)},
#         'node2': {
#             'out': ('node1',),
#             'function': (lambda x: x),
#             'args': (2, )},
#         'node3': {
#             'out': ('node1', 'node2'),
#             'function': (lambda x: x),
#             'args': (3,)}
#     }

#     network = Network(NETWORK_ARCHITECTURE)

#     assert NETWORK_ARCHITECTURE.keys() == network.nodes.keys()

# for name, node in network.nodes.items():
#     assert name == node.name
#     # outpipes
#     assert TOPOLOGY[name] == tuple(node.out_pipes.keys())

#     topology_in_pipes = [topology_name for topology_name,
#                          topology_out_pipes in TOPOLOGY.items() if name in topology_out_pipes]
#     assert tuple(topology_in_pipes) == tuple(node.in_pipes.keys())
