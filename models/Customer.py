from models.BaseEntity import BaseEntity
import exceptions
from exceptions import *  # noqa: F403


class Customer(BaseEntity):
    """
    Represents a customer in the system.
    Inherits from BaseEntity.

    Attributes:
        _entity_id (int): The customer's unique identifier.
        _entity_name (str): The customer's name.
        __email (str): The customer's email address (encapsulated).
        __phone (str): The customer's phone number (encapsulated).
    """

    def __init__(self, customer_id, customer_name, email, phone):
        """
        Initializes a Customer instance and validates the input data.

        Args:
            customer_id (int): The unique ID.
            customer_name (str): The name of the customer.
            email (str): The email address.
            phone (str): The phone number.

        Raises:
            CustomerNameError: If the name is empty.
            EmailError: If the email does not contain '@'.
            PhoneError: If the phone number is 7 characters or less.
            CustomerIDError: If the ID is less than or equal to 0.
        """
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
        """Returns the customer's name."""
        return self._entity_name

    def get_email(self):
        """Returns the customer's email."""
        return self.__email

    def get_phone(self):
        """Returns the customer's phone number."""
        return self.__phone

    def get_customer_id(self):
        """Returns the customer's ID."""
        return self._entity_id

    def set_email(self, email):
        """Updates the customer's email."""
        self.__email = email

    def set_phone(self, phone):
        """Updates the customer's phone number."""
        self.__phone = phone

    def show_info(self):
        """
        Returns a formatted string containing the customer's details.

        Returns:
            str: Customer information.
        """
        return (
            f"CUSTOMER INFO\n"
            f"Name: {self._entity_name}\n"
            f"Email: {self.__email}\n"
            f"Phone: {self.__phone}"
        )
