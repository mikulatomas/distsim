import pytest
from distsim import Network


def test_exception_network_architecture_not_dict():
    with pytest.raises(ValueError) as excinfo:
        Network("wrong type", '.')

    assert "Network architecture must be a dict" in str(excinfo.value)


def test_exception_arguments_not_tuple():
    with pytest.raises(ValueError) as excinfo:
        NETWORK_ARCHITECTURE = {
            'node1': {
                'out': {'node2', 'node3'},
                'function': (lambda x: x),
                'args': [1, ]}
        }
        Network(NETWORK_ARCHITECTURE, '.')

    assert "node args must be a tuple not" in str(excinfo.value)


def test_exception_wrong_out_node_name():
    with pytest.raises(ValueError) as excinfo:
        NETWORK_ARCHITECTURE = {
            'node1': {
                'out': {'node2', },
                'function': (lambda x: x),
                'args': (1, )}
        }
        Network(NETWORK_ARCHITECTURE, '.')

    assert "Target node" in str(excinfo.value)


def test_exception_function_not_callable():
    with pytest.raises(ValueError) as excinfo:
        NETWORK_ARCHITECTURE = {
            'node1': {
                'out': {'node2', },
                'function': "this is not a function",
                'args': (1, )}
        }
        Network(NETWORK_ARCHITECTURE, '.')

    assert "node function must be a callable" in str(excinfo.value)


def test_exception_architecture_not_complete():
    with pytest.raises(ValueError) as excinfo:
        NETWORK_ARCHITECTURE = {
            'node1': {
                'out': {'node2', },
            }}
        Network(NETWORK_ARCHITECTURE, '.')

    assert "in the network architecture must include 'out', 'function' and 'args' values." in str(
        excinfo.value)
