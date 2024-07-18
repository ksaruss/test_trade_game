from objects.base_object import Base_object


class Company(Base_object):
    def __init__(self, id_: int):
        super().__init__(id_=id_)
