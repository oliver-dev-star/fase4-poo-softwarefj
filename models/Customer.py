from models.BaseEntity import BaseEntity
import exceptions
from exceptions import *  # noqa: F403


class Customer(BaseEntity):

    def __init__(self, customer_id, customer_name, email, phone):

        super().__init__(customer_id, customer_name)
        self.__email = email
        self.__phone = phone

        if not self._entity_name.strip():
            raise exceptions.CustomerNameError("Customer name cannot be empty")
        if "@" not in self.__email:
            raise exceptions.EmailError("Invalid email format")
        if len(self.__phone) <= 7:
            raise exceptions.PhoneError("Phone cannot be less than 8 characters")
        if self._entity_id <= 0:
            raise exceptions.CustomerIDError("Customer ID must be greater than 0")

    def get_name(self):
        return self._entity_name

    def get_email(self):
        return self.__email

    def get_phone(self):
        return self.__phone

    def get_customer_id(self):
        return self._entity_id

    def set_email(self, email):
        self.__email = email

    def set_phone(self, phone):
        self.__phone = phone

    def show_info(self):
        return (
            f"CUSTOMER INFO\n"
            f"Name: {self._entity_name}\n"
            f"Email: {self.__email}\n"
            f"Phone: {self.__phone}"
        )
