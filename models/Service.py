from models.BaseEntity import BaseEntity
from abc import ABC, abstractmethod


class Service(BaseEntity, ABC):
    """
    Abstract base class for all services offered by the company.
    Inherits from BaseEntity.

    Attributes:
        _entity_id (int): The service's unique identifier.
        _entity_name (str): The service's name.
        _service_price (float): The base price of the service.
    """

    def __init__(self, service_id, service_name, service_price):
        """
        Initializes a Service instance.

        Args:
            service_id (int): Unique service ID.
            service_name (str): Name of the service.
            service_price (float): Base price of the service.
        """
        super().__init__(service_id, service_name)
        self._service_price = service_price

    def get_service_id(self):
        """Returns the service ID."""
        return self._entity_id

    def get_service_name(self):
        """Returns the service name."""
        return self._entity_name

    def get_service_price(self):
        """Returns the base service price."""
        return self._service_price

    @abstractmethod
    def calculate_cost(self, quantity):
        """
        Abstract method to calculate the total cost based on quantity/duration.
        Must be implemented by subclasses (Polymorphism).

        Args:
            quantity (int/float): The amount, duration, or units of the service.
            
        Returns:
            float: The calculated cost.
        """
        pass


class RoomService(Service):
    """Represents a room reservation service."""

    def __init__(self, service_id, service_name, service_price):
        super().__init__(service_id, service_name, service_price)

    def calculate_cost(self, days):
        """Calculates cost based on the number of days."""
        return self._service_price * days

    def show_info(self):
        return f"SERVICE ROOM: {self._entity_name} | ID: {self._entity_id} | Daily Rate: ${self._service_price}"


class CleaningService(Service):
    """Represents a cleaning service."""
    
    def __init__(self, service_id, service_name, service_price):
        super().__init__(service_id, service_name, service_price)

    def calculate_cost(self, quantity):
        """Calculates cost based on the number of sessions."""
        return self._service_price * quantity

    def show_info(self):
        return f"SERVICE CLEANING: {self._entity_name} | ID: {self._entity_id} | Price per Session: ${self._service_price}"


class SpaService(Service):
    """Represents a spa service."""
    
    def __init__(self, service_id, service_name, service_price):
        super().__init__(service_id, service_name, service_price)

    def calculate_cost(self, hours):
        """Calculates cost based on the number of hours."""
        return self._service_price * hours

    def show_info(self):
        return f"SERVICE SPA: {self._entity_name} | ID: {self._entity_id} | Hourly Rate: ${self._service_price}"


class RentedService(Service):
    """Represents an equipment rental service."""
    
    def __init__(self, service_id, service_name, service_price):
        super().__init__(service_id, service_name, service_price)

    def calculate_cost(self, days):
        """Calculates cost based on rental days."""
        return self._service_price * days

    def show_info(self):
        return f"SERVICE [Rental]: {self._entity_name} | Daily Rate: ${self._service_price}"


class ConsultationService(Service):
    """Represents a professional consultation service."""
    
    def __init__(self, service_id, service_name, service_price):
        super().__init__(service_id, service_name, service_price)

    def calculate_cost(self, hours):
        """Calculates cost based on consultation hours."""
        return self._service_price * hours

    def show_info(self):
        return f"SERVICE [Consultation]: {self._entity_name} | Hourly Rate: ${self._service_price}"
