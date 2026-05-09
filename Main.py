import os
import logging
import tkinter as tk
from models.Reservation import Reservation
from models.Service import (
    RoomService,
    SpaService,
    CleaningService,
    RentedService,
    ConsultationService,
)
from models.Customer import Customer
from gui import SoftwareFJ_GUI

# --- Setup Logging ---
log_dir = "logs"
if not os.path.exists(log_dir):
    os.makedirs(log_dir)
    print(f"Directory '{log_dir}' created successfully.")

logging.basicConfig(
    filename=os.path.join(log_dir, "software_fj.log"),
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

def save_error_to_file(error):
    """Logs captured exceptions to a file."""
    logging.error(f"Captured Exception: {type(error).__name__} - {error}")

# --- Simulation Logic ---
def execute_simulation(scenario):
    """
    Executes a specific simulation scenario, handling exceptions robustly.
    Uses try/except/else/finally structures.
    """
    valid_customers = []
    valid_services = []
    valid_reservations = []

    # --- Data Sets based on Scenario ---
    if scenario == "sim1":
        customer_data = [
            {"id": 1, "name": "Juan Gutierrez", "email": "juan@unad.edu.co", "phone": "3001234567"},
            {"id": 2, "name": "Angel Mauricio", "email": "invalid-email", "phone": "123"},
        ]
        service_data = [
            {"id": 101, "name": "Deluxe Room", "price": 150, "type": "room"},
            {"id": -5, "name": "Bad Service", "price": 0, "type": "spa"}, 
            {"id": 102, "name": "Professional Consultation", "price": 200, "type": "consultation"},
        ]
        reservation_attempts = [
            {"id": 501, "in": "2025-10-01", "out": "2025-10-05", "qty": 3, "s_idx": 0},
            {"id": 502, "in": "2025-12-20", "out": "2025-12-15", "qty": 1, "s_idx": 0},
        ]
    elif scenario == "sim2":
        customer_data = [
            {"id": -1, "name": "", "email": "no-at-sign.com", "phone": "12"},
            {"id": 3, "name": "Oliver", "email": "oliver@mail.com", "phone": "3109876543"},
        ]
        service_data = [
            {"id": 103, "name": "Laptop Rental", "price": 50, "type": "rented"},
        ]
        reservation_attempts = [
            {"id": 503, "in": "bad-date-format", "out": "2025-11-02", "qty": 5, "s_idx": 0},
            {"id": -10, "in": "2025-11-01", "out": "2025-11-02", "qty": -5, "s_idx": 0},
        ]
    else: 
        customer_data = [
            {"id": 10, "name": "Alice Smith", "email": "alice@company.com", "phone": "5551234567"},
        ]
        service_data = [
            {"id": 201, "name": "Conference Room A", "price": 300, "type": "room"},
            {"id": 202, "name": "Projector Rental", "price": 25, "type": "rented"},
        ]
        reservation_attempts = [
            {"id": 901, "in": "2026-01-10", "out": "2026-01-12", "qty": 2, "s_idx": 0},
            {"id": 902, "in": "2026-01-10", "out": "2026-01-11", "qty": 1, "s_idx": 1},
        ]

    # --- Execution Blocks ---
    print("--- Processing Customers ---")
    for data in customer_data:
        try:
            client = Customer(data["id"], data["name"], data["email"], data["phone"])
        except Exception as e:
            print(f"[ERROR] Failed to create customer {data.get('name', 'Unknown')}: {e}")
            save_error_to_file(e)
        else:
            print(f"[SUCCESS] Customer {data['name']} registered.")
            valid_customers.append(client)
        finally:
            print(f"Finished processing ID: {data['id']}")

    print("\n--- Processing Services ---")
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

    print("\n--- Processing Reservations ---")
    if valid_customers and valid_services:
        for res in reservation_attempts:
            try:
                s_index = res["s_idx"] % len(valid_services) 
                
                r = Reservation(
                    res["id"], res["in"], res["out"],
                    valid_customers[0], valid_services[s_index], res["qty"],
                )
            except Exception as e:
                print(f"[ERROR] Reservation {res['id']} failed: {e}")
                save_error_to_file(e)
            else:
                try:
                    r.confirm_reservation()
                    print(f"[SUCCESS] Reservation {res['id']} confirmed.")
                    valid_reservations.append(r)
                except Exception as e:
                     print(f"[ERROR] Could not confirm reservation: {e}")
                     save_error_to_file(e)
    else:
         print("[WARNING] Skipping reservations. Need at least 1 valid customer and 1 valid service.")

    # --- FINAL REPORT ---
    print("\n" + "=" * 40)
    print(f" FINAL SYSTEM STATUS REPORT ({scenario})")
    print("=" * 40)
    print(f"Valid Customers Created: {len(valid_customers)}")
    print(f"Valid Services Created: {len(valid_services)}")
    print(f"Active Reservations: {len(valid_reservations)}")
    
    print("\n[RESERVATION DETAILS]")
    for r in valid_reservations:
        print("-" * 20)
        print(r)
        print(f"Cost with 10% tax: ${r.calculate_total_cost(tax_rate=0.10)}")

    print("\nSimulation Complete.\n")

def main():
    """Application entry point."""
    root = tk.Tk()
    app = SoftwareFJ_GUI(root, execute_simulation)
    root.mainloop()

if __name__ == "__main__":
    main()
