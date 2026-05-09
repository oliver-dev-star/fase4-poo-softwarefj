from models.BaseEntity import BaseEntity
from abc import ABC, abstractmethod


class Service(BaseEntity, ABC):

    def __init__(self, service_id, service_name, service_price):
        super().__init__(service_id, service_name)
        self._service_price = service_price

    def get_service_id(self):
        return self._entity_id

    def get_service_name(self):
        return self._entity_name

    def get_service_price(self):
        return self._service_price

    @abstractmethod
    def calculate_cost(self, quantity):
        pass


class RoomService(Service):

    def __init__(self, service_id, service_name, service_price):
        super().__init__(service_id, service_name, service_price)

    def calculate_cost(self, days):
        return self._service_price * days

    def show_info(self):
        # Overridden method from BaseEntity
        return f"SERVICE ROOM: {self._entity_name} | ID: {self._entity_id} | Daily Rate: ${self._service_price}"


class CleaningService(Service):
    def __init__(self, service_id, service_name, service_price):
        super().__init__(service_id, service_name, service_price)

    def calculate_cost(self, quantity):
        return self._service_price * quantity

    def show_info(self):
        return f"SERVICE CLEANING: {self._entity_name} | ID: {self._entity_id} | Price per Session: ${self._service_price}"


class SpaService(Service):
    def __init__(self, service_id, service_name, service_price):
        super().__init__(service_id, service_name, service_price)

    def calculate_cost(self, hours):
        return self._service_price * hours

    def show_info(self):
        return f"SERVICE SPA: {self._entity_name} | ID: {self._entity_id} | Hourly Rate: ${self._service_price}"


class RentedService(Service):
    def __init__(self, service_id, service_name, service_price):
        super().__init__(service_id, service_name, service_price)

    def calculate_cost(self, days):
        return self._service_price * days


class ConsultationService(Service):
    def __init__(self, service_id, service_name, service_price):
        super().__init__(service_id, service_name, service_price)

    def calculate_cost(self, hours):
        return self._service_price * hours
