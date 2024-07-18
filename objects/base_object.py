from values import Values


class Base_object:
    def __init__(self, id_: int):
        self._id = id_
        self.values: 'Values' = Values()

