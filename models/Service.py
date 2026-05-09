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
        _billing_type (str): Defines how the service is billed ('days' or 'hours').
    """

    def __init__(self, service_id, service_name, service_price, billing_type):
        """
        Initializes a Service instance.

        Args:
            service_id (int): Unique service ID.
            service_name (str): Name of the service.
            service_price (float): Base price or rate of the service.
            billing_type (str): The billing strategy, either 'days' or 'hours'.
        """
        super().__init__(service_id, service_name)
        self._service_price = service_price
        self._billing_type = billing_type

    def get_service_id(self):
        """
        Retrieves the service ID.
        
        Returns:
            int: The unique service identifier.
        """
        return self._entity_id

    def get_service_name(self):
        """
        Retrieves the service name.
        
        Returns:
            str: The name of the service.
        """
        return self._entity_name

    def get_service_price(self):
        """
        Retrieves the base service price.
        
        Returns:
            float: The service rate/price.
        """
        return self._service_price

    def get_billing_type(self):
        """
        Retrieves the billing mode of the service.
        
        Returns:
            str: The billing type ('days' or 'hours').
        """
        return self._billing_type

    @abstractmethod
    def calculate_cost(self, quantity):
        """
        Abstract method to calculate the total cost.
        Must be implemented by concrete subclass to handle days or hours.

        Args:
            quantity (int/float): The duration or amount of service required.
        """
        pass


class RoomService(Service):
    """Represents a standard room reservation service billed by days."""
    def __init__(self, service_id, service_name, service_price):
        super().__init__(service_id, service_name, service_price, 'days')

    def calculate_cost(self, days):
        """Calculates total cost based on the number of days reserved."""
        return self._service_price * days

    def show_info(self):
        """Returns formatted details about the room service."""
        return f"SERVICE ROOM: {self._entity_name} | ID: {self._entity_id} | Daily Rate: ${self._service_price}"


class CleaningService(Service):
    """Represents a cleaning service billed by hours."""
    def __init__(self, service_id, service_name, service_price):
        super().__init__(service_id, service_name, service_price, 'hours')

    def calculate_cost(self, hours):
        """Calculates total cost based on the number of hours requested."""
        return self._service_price * hours

    def show_info(self):
        """Returns formatted details about the cleaning service."""
        return f"SERVICE CLEANING: {self._entity_name} | ID: {self._entity_id} | Hourly Rate: ${self._service_price}"


class SpaService(Service):
    """Represents a spa service billed by hours."""
    def __init__(self, service_id, service_name, service_price):
        super().__init__(service_id, service_name, service_price, 'hours')

    def calculate_cost(self, hours):
        """Calculates total cost based on the number of spa hours."""
        return self._service_price * hours

    def show_info(self):
        """Returns formatted details about the spa service."""
        return f"SERVICE SPA: {self._entity_name} | ID: {self._entity_id} | Hourly Rate: ${self._service_price}"


class RentedService(Service):
    """Represents an equipment rental service billed by days."""
    def __init__(self, service_id, service_name, service_price):
        super().__init__(service_id, service_name, service_price, 'days')

    def calculate_cost(self, days):
        """Calculates total cost based on the number of rented days."""
        return self._service_price * days

    def show_info(self):
        """Returns formatted details about the rental service."""
        return f"SERVICE [Rental]: {self._entity_name} | Daily Rate: ${self._service_price}"


class ConsultationService(Service):
    """Represents a professional consultation service billed by hours."""
    def __init__(self, service_id, service_name, service_price):
        super().__init__(service_id, service_name, service_price, 'hours')

    def calculate_cost(self, hours):
        """Calculates total cost based on the number of consultation hours."""
        return self._service_price * hours

    def show_info(self):
        """Returns formatted details about the consultation service."""
        return f"SERVICE [Consultation]: {self._entity_name} | Hourly Rate: ${self._service_price}"


class CustomDailyService(Service):
    """
    A dynamically generated generic service billed by days.
    Allows administrators to add new types of daily services at runtime.
    """
    def __init__(self, service_id, service_name, service_price):
        super().__init__(service_id, service_name, service_price, 'days')

    def calculate_cost(self, days):
        """Calculates total cost based on the custom daily rate."""
        return self._service_price * days

    def show_info(self):
        """Returns formatted details about the custom daily service."""
        return f"SERVICE CUSTOM [Days]: {self._entity_name} | ID: {self._entity_id} | Daily Rate: ${self._service_price}"


class CustomHourlyService(Service):
    """
    A dynamically generated generic service billed by hours.
    Allows administrators to add new types of hourly services at runtime.
    """
    def __init__(self, service_id, service_name, service_price):
        super().__init__(service_id, service_name, service_price, 'hours')

    def calculate_cost(self, hours):
        """Calculates total cost based on the custom hourly rate."""
        return self._service_price * hours

    def show_info(self):
        """Returns formatted details about the custom hourly service."""
        return f"SERVICE CUSTOM [Hours]: {self._entity_name} | ID: {self._entity_id} | Hourly Rate: ${self._service_price}"
