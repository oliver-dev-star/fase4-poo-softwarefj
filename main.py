from reservation import Reservation
from service import RoomService, SpaService
from Customer import Customer

#Save errors to file

def save_error_to_file(error_message):
    with open("logs.txt", "a") as file:
        file.write(str(error_message)+"\n")

#Creation of customers


try:
    customer1 = Customer(1, "John Doe", "john.doe@example.com", "123456789")
    print("Customer 1 created successfully\n")
except Exception as e:
    print("Error creating customer 1:\n", e)
    save_error_to_file(e)

try:
    customer2 = Customer(2, "Jane Doe", "jane.doe@example.com", "987654321")
    print("Customer 2 created successfully\n")
except Exception as e:
    print("Error creating customer 2:", e)
    save_error_to_file(e)



#Creation of services

try:
    room1 = RoomService(1, "Room", 100)
    print("Room 1 created successfully\n")
except Exception as e:
    print("Error creating room 1:\n", e)
    save_error_to_file(e)   

try:
    spa1 = SpaService(1, "Spa", 50)
    print("Spa 1 created successfully\n")
except Exception as e:
    print("Error creating spa 1:", e)
    save_error_to_file(e)   

# Reservation

try:
    reservation1 = Reservation(1,
     "2025-10-10", 
     "2025-10-15",
     customer1,
     room1,
     5
    )

    print("Reservation 1 created successfully\n")
except Exception as e:
    print("Error creating reservation 1:\n", e)
    save_error_to_file(e)

try:
    reservation2 = Reservation(2,
     "2025-10-10", 
     "2025-10-15",
     customer2,
     spa1,
     3
    )
    print("Reservation 2 created successfully\n")
except Exception as e:
    print("Error creating reservation 2:\n", e)
    save_error_to_file(e)

try:
    bad_reservation = Reservation(
        3, "2025-10-20", "2025-10-10",
        customer1, room1, 2
    )
except Exception as e:
    print("Reservation error:", e)
    save_error_to_file(e)

reservation1.confirm_reservation()
reservation2.confirm_reservation()


#Visual errors with customers

try:
    customer3 = Customer(1, "John Doe", "manzana", "1234")
except Exception as e:
    print("Error printing customer 3:\n", e)

try:
    customer3 = Customer("", "Pera", "1234568789")
except TypeError:
    print("Error printing customer 2: Missing required arguments")
except Exception as e:
    print("Error printing customer 2:\n", e)


# Test

print("========================================")
print("Software FJ Reservation System")
print("========================================")
print("")
print("----Customers -----\n")
print(customer1)
print(customer2)
print("")
print("----Services -----\n")
print(room1)
print(spa1)
print("")
print("----Reservations -----\n")
print(reservation1)
print("")   
print(reservation2)
print("")

