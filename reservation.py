from exceptions import *
from Customer import Customer
from service import Service



class Reservation:
    def __init__(self, reservation_id, check_in_date, check_out_date, customer, service, quantity):

        if service is None:
            raise ReservationServiceError("Service cannot be None")
        if check_in_date > check_out_date:
            raise ReservationDateError("Check-in date must be before check-out date")
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

    def calculate_total_cost(self):
        
        return self._service.calculate_cost(self._quantity)

    def __str__(self):
        return self.show_info()

    def show_info(self):
        return f"Reservation ID: {self._reservation_id}\nCheck-in date: {self._check_in_date}\nCheck-out date: {self._check_out_date}\nCustomer: {self._customer}\nService: {self._service}\nQuantity: {self._quantity}\nTotal cost: {self.calculate_total_cost()}\nStatus: {self._status}"
        