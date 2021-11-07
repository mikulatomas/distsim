import typing


class NodeDefinition:
    def __init__(
        self,
        name: str,
        function: typing.Callable,
        args: typing.Collection = (),
        connections: typing.Collection = (),
    ) -> None:
        self.name = name
        self.function = function
        self.args = args
        self.connections = connections