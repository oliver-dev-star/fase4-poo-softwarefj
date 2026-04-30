from abc import ABC, abstractmethod

class Service(ABC):

    def __init__(self, service_id, service_name, service_price):
        self._service_id = service_id
        self._service_name = service_name
        self._service_price = service_price

    def get_service_id(self):
        return self._service_id

    def get_service_name(self):
        return self._service_name

    def get_service_price(self):
        return self._service_price
    
    def __str__(self):
        return f"Service Name: {self._service_name}\nService Price: {self._service_price}"

    @abstractmethod
    def calculate_cost(self, quantity):
        pass


class RoomService(Service):

    def __init__(self, service_id, service_name, service_price):
        super().__init__(service_id, service_name, service_price)
    
    def get_service_name(self):
        return self._service_name
    
    def calculate_cost(self, days):
        return self._service_price * days

class CleaningService(Service):
    def __init__(self, service_id, service_name, service_price):
        super().__init__(service_id, service_name, service_price)
    
    def calculate_cost(self, quantity):
        return self._service_price * quantity

class SpaService(Service):
    def __init__(self, service_id, service_name, service_price):
        super().__init__(service_id, service_name, service_price)
    
    def calculate_cost(self, hours):
        return self._service_price * hours