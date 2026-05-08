import logging
from datetime import datetime
from models.Reservation import Reservation
from models.Service import RoomService, SpaService, CleaningService
from models.Customer import Customer

# Save errors to file


def save_error_to_file(error):
    logging.error(f"Captured Exception: {type(error).__name__} - {error}")


logging.basicConfig(
    filename="logs/software_fj.log",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

# Creation of customers


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
            "name": "Jane Doe",
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
            c = Customer(data["id"], data["name"], data["email"], data["phone"])
        except Exception as e:
            print(f"[ERROR] Failed to create customer {data['name']}: {e}")
            save_error_to_file(e)
        else:
            print(f"[SUCCESS] Customer {data['name']} registered.")
            valid_customers.append(c)
        finally:
            print(f"Finished processing ID: {data['id']}")

    service_data = [
        {"id": 101, "name": "Deluxe Room", "price": 150, "type": "room"},  # Valid
        {"id": -5, "name": "Bad Service", "price": 0, "type": "spa"},  # Invalid
        {"id": 102, "name": "Full Cleaning", "price": 80, "type": "clean"},  # Valid
    ]

    print("\n--- [TEST] Processing Services ---")
    for s_data in service_data:
        try:
            if s_data["type"] == "room":
                s = RoomService(s_data["id"], s_data["name"], s_data["price"])
            elif s_data["type"] == "spa":
                s = SpaService(s_data["id"], s_data["name"], s_data["price"])
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
        {"id": 501, "in": "2025-10-01", "out": "2025-10-05", "qty": 3},  # Valid
        {
            "id": 502,
            "in": "2025-12-20",
            "out": "2025-12-15",
            "qty": 1,
        },  # Invalid (Dates)
        {
            "id": 503,
            "in": "2025-11-01",
            "out": "2025-11-02",
            "qty": -5,
        },  # Invalid (Quantity)
        {"id": 504, "in": "2025-09-01", "out": "2025-09-10", "qty": 2},  # Valid
    ]

    print("\n--- [TEST] Processing Reservations ---")
    for i, res in enumerate(reservation_attempts):
        try:
            r = Reservation(
                res["id"],
                res["in"],
                res["out"],
                valid_customers[0],
                valid_services[0],
                res["qty"],
            )
        except IndexError:
            print(
                "[ERROR] There are no valid customers or services to make the reservation."
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
