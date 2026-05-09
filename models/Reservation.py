from datetime import datetime
from models.Customer import Customer
from models.Service import Service
from exceptions import *


class Reservation:
    """
    Manages the booking of a service by a customer.
    Handles date parsing, validation, and cost calculation.

    Attributes:
        _reservation_id (int): Unique identifier for the reservation.
        _check_in_date (str): Start date/time of the reservation.
        _check_out_date (str): End date/time of the reservation.
        _customer (Customer): The customer holding the reservation.
        _service (Service): The service being reserved.
        _quantity (int): The duration (days or hours) of the reservation.
        _status (str): Current reservation status ('pending', 'confirmed', 'cancelled').
    """

    def __init__(
        self, reservation_id, check_in_date, check_out_date, customer, service, quantity
    ):
        """
        Initializes a Reservation instance and applies business logic validations.

        Args:
            reservation_id (int): Unique ID of the reservation.
            check_in_date (str): Start date string (Format: YYYY-MM-DD or YYYY-MM-DD HH:MM).
            check_out_date (str): End date string (Format: YYYY-MM-DD or YYYY-MM-DD HH:MM).
            customer (Customer): The related Customer object.
            service (Service): The related Service object.
            quantity (int): Duration in days or hours.

        Raises:
            ReservationServiceError: If service is None or not a Service instance.
            ReservationDateError: If date parsing fails or check-in is after check-out.
            ReservationQuantityError: If quantity is 0 or negative.
            ReservationIDError: If the reservation ID is invalid.
            ReservationCustomerError: If customer is invalid.
        """
        if service is None:
            raise ReservationServiceError("Service cannot be None")

        def parse_date(d_str):
            """
            Internal helper function to parse dates.
            Supports exact datetime formatting or legacy daily formatting to ensure
            backward compatibility with existing automated simulations.
            """
            for fmt in ("%Y-%m-%d %H:%M", "%Y-%m-%d"):
                try:
                    return datetime.strptime(d_str, fmt)
                except ValueError:
                    pass
            raise ValueError(f"Time data '{d_str}' does not match expected formats.")

        try:
            start = parse_date(check_in_date)
            end = parse_date(check_out_date)

            if start > end:
                raise ReservationDateError("Check-in/Start time must be before check-out/End time")
        except ValueError as e:
            # Demonstrating Exception Chaining
            raise ReservationDateError(f"Invalid date format: {e}") from e

        if quantity <= 0:
            raise ReservationQuantityError("Quantity must be greater than 0")

        if reservation_id <= 0:
            raise ReservationIDError("Reservation ID must be greater than 0")

        if not isinstance(customer, Customer):
            raise ReservationCustomerError("Customer must be an instance of Customer class")

        if not isinstance(service, Service):
            raise ReservationServiceError("Service must be an instance of Service class")

        self._reservation_id = reservation_id
        self._check_in_date = check_in_date
        self._check_out_date = check_out_date
        self._customer = customer
        self._service = service
        self._quantity = quantity
        self._status = "pending"

    def confirm_reservation(self):
        """
        Changes the status of the reservation to 'confirmed'.

        Raises:
            ReservationStatusError: If the reservation has already been cancelled.
        """
        if self._status == "cancelled":
            raise ReservationStatusError("Reservation is cancelled and cannot be confirmed")
        self._status = "confirmed"

    def cancel_reservation(self):
        """
        Changes the status of the reservation to 'cancelled'.

        Raises:
            ReservationStatusError: If the reservation is already cancelled.
        """
        if self._status == "cancelled":
            raise ReservationStatusError("Reservation is already cancelled")
        self._status = "cancelled"

    def get_reservation_id(self):
        """Returns the reservation ID."""
        return self._reservation_id

    def get_check_in_date(self):
        """Returns the check-in date/time."""
        return self._check_in_date

    def get_check_out_date(self):
        """Returns the check-out date/time."""
        return self._check_out_date

    def get_customer(self):
        """Returns the associated Customer object."""
        return self._customer

    def get_service(self):
        """Returns the associated Service object."""
        return self._service

    def get_quantity(self):
        """Returns the requested duration or quantity."""
        return self._quantity

    def calculate_total_cost(self, discount=0, tax_rate=0.0):
        """
        Calculates the final cost for the reservation by interacting with the
        associated service's cost calculation strategy. 
        Demonstrates method overloading via default arguments.

        Args:
            discount (float, optional): Fixed discount amount to subtract. Defaults to 0.
            tax_rate (float, optional): Decimal representing tax percentage. Defaults to 0.0.

        Returns:
            float: The total calculated cost.
        """
        base_cost = self._service.calculate_cost(self._quantity)
        total = base_cost - discount
        total += total * tax_rate
        return total

    def show_info(self):
        """
        Formats and returns the full details of the reservation.

        Returns:
            str: A multi-line string containing reservation details.
        """
        total = self.calculate_total_cost()
        return (
            f"RESERVATION DETAILS\n"
            f"ID: {self._reservation_id}\n"
            f"Status: {self._status.upper()}\n"
            f"Dates/Time: {self._check_in_date} to {self._check_out_date}\n"
            f"Client: {self._customer.get_name()} \n"
            f"Service: {self._service.get_service_name()}\n"
            f"Total Cost: ${total}"
        )

    def __str__(self):
        """String representation of the reservation (delegates to show_info)."""
        return self.show_info()
