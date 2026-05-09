"""
Custom Exception Classes for Software FJ
Demonstrates advanced exception handling requirements.
"""

class AppError(Exception):
    """Base class for general application errors."""
    pass

# --- Customer Exceptions ---

class CustomerNameError(Exception):
    """Raised when customer name is invalid."""
    pass

class CustomerIDError(Exception):
    """Raised when customer ID is invalid."""
    pass

class EmailError(Exception):
    """Raised when email format is invalid."""
    pass

class PhoneError(Exception):
    """Raised when phone number format is invalid."""
    pass

# --- Service Exceptions ---

class ServiceError(Exception):
    """Base class for service-related errors."""
    pass

class ServiceNameError(Exception):
    """Raised when service name is invalid."""
    pass

class ServiceIDError(Exception):
    """Raised when service ID is invalid."""
    pass

class ServicePriceError(Exception):
    """Raised when service price is invalid."""
    pass

class ServiceUnavailableError(Exception):
    """Raised when a requested service is not available."""
    pass

# --- Reservation Exceptions ---

class ReservationError(Exception):
    """Base class for reservation-related errors."""
    pass

class ReservationIDError(Exception):
    """Raised when reservation ID is invalid."""
    pass

class ReservationStatusError(Exception):
    """Raised when attempting an invalid status transition."""
    pass

class ReservationDateError(Exception):
    """Raised when check-in/out dates are invalid or logically incorrect."""
    pass

class ReservationQuantityError(Exception):
    """Raised when quantity is invalid."""
    pass

class ReservationServiceError(Exception):
    """Raised when the assigned service is invalid."""
    pass

class ReservationCustomerError(Exception):
    """Raised when the assigned customer is invalid."""
    pass

class ReservationNotFoundError(Exception):
    """Raised when a reservation cannot be found."""
    pass

class DurationError(Exception):
    """Raised when the duration of a service is invalid."""
    pass
