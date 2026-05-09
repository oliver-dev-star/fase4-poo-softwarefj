from abc import ABC, abstractmethod


class BaseEntity(ABC):
    """
    Abstract base class for all entities in the system.
    
    Attributes:
        _entity_id (int): The unique identifier for the entity.
        _entity_name (str): The name of the entity.
    """

    def __init__(self, entity_id, entity_name):
        """
        Initializes the BaseEntity.

        Args:
            entity_id (int): The unique identifier for the entity.
            entity_name (str): The name of the entity.
        """
        self._entity_id = entity_id
        self._entity_name = entity_name

    @abstractmethod
    def show_info(self):
        """
        Abstract method to display the entity's information.
        Must be implemented by subclasses.

        Returns:
            str: A formatted string containing the entity's details.
        """
        pass

    def __str__(self):
        """
        String representation of the entity.

        Returns:
            str: The result of the show_info() method.
        """
        return self.show_info()
