from abc import ABC, abstractmethod


class BaseEntity(ABC):
    def __init__(self, entity_id, entity_name):
        self._entity_id = entity_id
        self._entity_name = entity_name

    @abstractmethod
    def show_info(self):
        pass

    def __str__(self):
        return self.show_info()
