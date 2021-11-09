# distsim

Simulator of distributed system based on Python `multiprocessing.Process` and `multiprocessing.Pipe` communication.

## Installation
```bash
$ pip install distsim
```

## Examples
See `examples/` folder.

* `simple_network/` - basic network with two interconnected nodes. One message per node is sent and received.
* `nodes_with_arguments/` - two nodes, no links, each accepts one argument.
* `receive_any/` - demonstration of `Node.receive_any()` method.
* `threads/` - demonstration of spawning threads inside `Node` instance.