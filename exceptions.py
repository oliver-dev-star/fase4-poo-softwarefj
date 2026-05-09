# General Errors


class AppError(Exception):
    pass


# Costumers


class CustomerNameError(Exception):
    pass


class CustomerIDError(Exception):
    pass


class EmailError(Exception):
    pass


class PhoneError(Exception):
    pass


# Services


class ServiceError(Exception):
    pass


class ServiceNameError(Exception):
    pass


class ServiceIDError(Exception):
    pass


class ServicePriceError(Exception):
    pass


class ServiceUnavailableError(Exception):
    pass


# Reservations


class ReservationError(Exception):
    pass


class ReservationIDError(Exception):
    pass


class ReservationStatusError(Exception):
    pass


class ReservationDateError(Exception):
    pass


class ReservationQuantityError(Exception):
    pass


class ReservationServiceError(Exception):
    pass


class ReservationCustomerError(Exception):
    pass


class ReservationNotFoundError(Exception):
    pass


class DurationError(Exception):
    pass
