from datetime import datetime
from models.Customer import Customer
from models.Service import Service
from exceptions import *


class Reservation:
    """
    Manages the booking of a service by a customer.

    Attributes:
        _reservation_id (int): Unique identifier.
        _check_in_date (str): Start date (YYYY-MM-DD).
        _check_out_date (str): End date (YYYY-MM-DD).
        _customer (Customer): The customer making the reservation.
        _service (Service): The requested service.
        _quantity (int): Duration or amount for the service.
        _status (str): Current status ('pending', 'confirmed', 'cancelled').
    """

    def __init__(
        self, reservation_id, check_in_date, check_out_date, customer, service, quantity
    ):
        """
        Initializes a Reservation and validates all input parameters.

        Args:
            reservation_id (int): ID of the reservation.
            check_in_date (str): Start date string.
            check_out_date (str): End date string.
            customer (Customer): Instance of Customer.
            service (Service): Instance of Service.
            quantity (int): Units of service requested.

        Raises:
            ReservationServiceError: If service is None or not a Service instance.
            ReservationDateError: If date format is wrong or check-in is after check-out.
            ReservationQuantityError: If quantity is <= 0.
            ReservationIDError: If reservation_id is <= 0.
            ReservationCustomerError: If customer is not a Customer instance.
        """
        if service is None:
            raise ReservationServiceError("Service cannot be None")

        try:
            date_format = "%Y-%m-%d"
            start = datetime.strptime(check_in_date, date_format)
            end = datetime.strptime(check_out_date, date_format)

            if start > end:
                raise ReservationDateError(
                    "Check-in date must be before check-out date"
                )
        # Exception Chaining example
        except ValueError as e:
            raise ReservationDateError(f"Invalid date format: {e}") from e

        if quantity <= 0:
            raise ReservationQuantityError("Quantity must be greater than 0")

        if reservation_id <= 0:
            raise ReservationIDError("Reservation ID must be greater than 0")

        if not isinstance(customer, Customer):
            raise ReservationCustomerError(
                "Customer must be an instance of Customer class"
            )

        if not isinstance(service, Service):
            raise ReservationServiceError(
                "Service must be an instance of Service class"
            )

        self._reservation_id = reservation_id
        self._check_in_date = check_in_date
        self._check_out_date = check_out_date
        self._customer = customer
        self._service = service
        self._quantity = quantity
        self._status = "pending"

    def confirm_reservation(self):
        """Confirms the reservation if it is not already cancelled."""
        if self._status == "cancelled":
            raise ReservationStatusError("Reservation is cancelled and cannot be confirmed")
        self._status = "confirmed"

    def cancel_reservation(self):
        """Cancels the reservation."""
        if self._status == "cancelled":
            raise ReservationStatusError("Reservation is already cancelled")
        self._status = "cancelled"

    def get_reservation_id(self):
        return self._reservation_id

    def get_check_in_date(self):
        return self._check_in_date

    def get_check_out_date(self):
        return self._check_out_date

    def get_customer(self):
        return self._customer

    def get_service(self):
        return self._service

    def get_quantity(self):
        return self._quantity

    def calculate_total_cost(self, discount=0, tax_rate=0.0):
        """
        Calculates the total cost with optional discount and taxes.
        Demonstrates method overloading concept through default parameters.

        Args:
            discount (float, optional): Fixed discount amount. Defaults to 0.
            tax_rate (float, optional): Tax rate as a decimal (e.g., 0.19 for 19%). Defaults to 0.0.

        Returns:
            float: Final calculated cost.
        """
        base_cost = self._service.calculate_cost(self._quantity)
        total = base_cost - discount
        total += total * tax_rate
        return total

    def show_info(self):
        """Displays formatted reservation details."""
        total = self.calculate_total_cost()
        return (
            f"RESERVATION DETAILS\n"
            f"ID: {self._reservation_id}\n"
            f"Status: {self._status.upper()}\n"
            f"Dates: {self._check_in_date} to {self._check_out_date}\n"
            f"Client: {self._customer.get_name()} \n"
            f"Service: {self._service.get_service_name()}\n"
            f"Total Cost: ${total}"
        )

    def __str__(self):
        return self.show_info()
