import pytest
from distsim import Network

NETWORK_ARCHITECTURES = [
    {
        'node1': {
            'out': {'node2', },
            'function': (lambda x: x),
            'args': (1,)},
        'node2': {
            'out': {'node1', },
            'function': (lambda x: x),
            'args': (2, )},
    },
    {
        'node1': {
            'out': {'node2', 'node1'},
            'function': (lambda x: x),
            'args': (1,)},
        'node2': {
            'out': {'node1', 'node2'},
            'function': (lambda x: x),
            'args': (2, )},
    },
    {
        'node1': {
            'out': set(),
            'function': (lambda x: x),
            'args': (1,)},
        'node2': {
            'out': {'node1'},
            'function': (lambda x: x),
            'args': (2, )},
    }
]


@ pytest.mark.parametrize("architecture", NETWORK_ARCHITECTURES)
def test_topology(architecture):

    network = Network(architecture, '.')

    assert architecture.keys() == network.nodes.keys()

    for node_name, metadata in architecture.items():
        assert set(
            network.nodes[node_name].out_pipes.keys()) == metadata['out']

    for node_name, node in network.nodes.items():
        for in_node_name in node.in_pipes.keys():
            assert node_name in architecture[in_node_name]['out']
