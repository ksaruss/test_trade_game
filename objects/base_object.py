from values import Values


class Base_object(Values):
    def __init__(self, id_: int):
        super().__init__()
        self._id = id_
