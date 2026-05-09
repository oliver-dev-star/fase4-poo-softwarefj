import logging
from models.Reservation import Reservation
from models.Service import (
    RoomService,
    SpaService,
    CleaningService,
    RentedService,
    ConsultationService,
)
from models.Customer import Customer

# Save errors to file

logging.basicConfig(
    filename="logs/software_fj.log",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


def save_error_to_file(error):
    logging.error(f"Captured Exception: {type(error).__name__} - {error}")


def run_test():
    print("========================================")
    print("   SOFTWARE FJ - INTEGRAL SYSTEM        ")
    print("========================================\n")

    valid_customers = []
    valid_services = []
    valid_reservations = []

    customer_data = [
        {
            "id": 1,
            "name": "Juan Gutierrez",
            "email": "juan@unad.edu.co",
            "phone": "3001234567",
        },  # valid
        {
            "id": 2,
            "name": "Angel mauricio",
            "email": "invalid-email",
            "phone": "123",
        },  # Invalid
        {
            "id": 3,
            "name": "Oliver",
            "email": "oliver@mail.com",
            "phone": "3109876543",
        },  # valid
    ]

    print("--- [TEST] Processing Customers ---")
    for data in customer_data:
        try:
            client = Customer(data["id"], data["name"], data["email"], data["phone"])
        except Exception as e:
            print(f"[ERROR] Failed to create customer {data['name']}: {e}")
            save_error_to_file(e)
        else:
            print(f"[SUCCESS] Customer {data['name']} registered.")
            valid_customers.append(client)
        finally:
            print(f"Finished processing ID: {data['id']}")

    # Test Services
    service_data = [
        {"id": 101, "name": "Deluxe Room", "price": 150, "type": "room"},  # Valid
        {"id": -5, "name": "Bad Service", "price": 0, "type": "spa"},  # Invalid
        {"id": 102, "name": "Full Cleaning", "price": 80, "type": "clean"},  # Valid
        {
            "id": 102,
            "name": "Professional Consultation",
            "price": 200,
            "type": "consultation",
        },
        {"id": 103, "name": "Laptop Rental", "price": 50, "type": "rented"},
    ]

    print("\n--- [TEST] Processing Services ---")
    for s_data in service_data:
        try:
            if s_data["type"] == "room":
                s = RoomService(s_data["id"], s_data["name"], s_data["price"])
            elif s_data["type"] == "spa":
                s = SpaService(s_data["id"], s_data["name"], s_data["price"])
            elif s_data["type"] == "consultation":
                s = ConsultationService(s_data["id"], s_data["name"], s_data["price"])
            elif s_data["type"] == "rented":
                s = RentedService(s_data["id"], s_data["name"], s_data["price"])
            else:
                s = CleaningService(s_data["id"], s_data["name"], s_data["price"])
        except Exception as e:
            print(f"[ERROR] Failed to create service {s_data['name']}: {e}")
            save_error_to_file(e)
        else:
            print(f"[SUCCESS] Service {s_data['name']} added.")
            valid_services.append(s)

    # Reservation Registry
    reservation_attempts = [
        {
            "id": 501,
            "in": "2025-10-01",
            "out": "2025-10-05",
            "qty": 3,
            "s_idx": 0,
        },  # Room
        {
            "id": 502,
            "in": "2025-12-20",
            "out": "2025-12-15",
            "qty": 1,
            "s_idx": 1,
        },  # Error dates
        {
            "id": 503,
            "in": "2025-11-01",
            "out": "2025-11-02",
            "qty": 5,
            "s_idx": 1,
        },  # Consultation
        {
            "id": 504,
            "in": "2025-09-01",
            "out": "2025-09-10",
            "qty": 2,
            "s_idx": 2,
        },  # Rented
    ]

    print("\n--- [TEST] Processing Reservations ---")
    for res in reservation_attempts:
        try:
            r = Reservation(
                res["id"],
                res["in"],
                res["out"],
                valid_customers[0],
                valid_services[res["s_idx"]],
                res["qty"],
            )
        except Exception as e:
            print(f"[ERROR] Reservation {res['id']} failed: {e}")
            save_error_to_file(e)
        else:
            r.confirm_reservation()
            print(f"[SUCCESS] Reservation {res['id']} confirmed.")
            valid_reservations.append(r)

    # --- FINAL REPORT ---
    print("\n" + "=" * 40)
    print("      FINAL SYSTEM STATUS REPORT")
    print("=" * 40)

    print("\n[ACTIVE RESERVATIONS]")

    for r in valid_reservations:
        print("-" * 20)
        print(r)


if __name__ == "__main__":
    run_test()
