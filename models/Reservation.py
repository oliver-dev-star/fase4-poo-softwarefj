from datetime import datetime
from models.Customer import Customer
from models.Service import Service
from exceptions import *


class Reservation:
    def __init__(
        self, reservation_id, check_in_date, check_out_date, customer, service, quantity
    ):

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
        if self._status == "Cancelled":
            raise ReservationStatusError("Reservation is cancelled")

        self._status = "confirmed"

    def cancel_reservation(self):
        if self._status == "Cancelled":
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
        base_cost = self._service.calculate_cost(self._quantity)
        total = base_cost - discount
        total += total * tax_rate
        return total

    def show_info(self):
        total = self.calculate_total_cost()
        return (
            f"RESERVATION DETAILS\n"
            f"ID: {self._reservation_id}\n"
            f"Status: {self._status.upper()}\n"
            f"Dates: {self._check_in_date} to {self._check_out_date}\n"
            f"Client: {self._customer.get_name()} \n"
            f"Total Cost: ${total}"
        )

    def __str__(self):
        return self.show_info()
