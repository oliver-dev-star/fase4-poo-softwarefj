# 🏢 Software FJ - Integral Management System

## 📄 Overview
This project is an **Object-Oriented, database-free integral system** designed for *Software FJ* to manage **clients, services, and reservations**.  
It fulfills academic requirements for:
- Advanced exception handling
- Class hierarchies
- Abstraction
- GUI implementation using **Tkinter**

---

## ✨ Key Features
- **Object-Oriented Architecture**  
  Heavy use of Abstraction (`BaseEntity`, `Service`), Inheritance, and Polymorphism.

- **Robust Exception Handling**  
  Implements custom exceptions (e.g., `CustomerNameError`, `ReservationDateError`), exception chaining, and extensive `try/except/else/finally` blocks.

- **Encapsulation**  
  Protects sensitive customer data (email, phone) using private attributes (`__email`).

- **Graphical User Interface (GUI)**  
  Tkinter-based interface that allows users to run automated simulation scenarios and view console outputs directly in the application.

- **Logging**  
  All captured exceptions are safely logged to `logs/software_fj.log` without crashing the application.

- **No Database**  
  All data is managed **in-memory** using Python lists and objects during the application's lifecycle.

---

## 🏗️ Architecture & Class Hierarchy
- **BaseEntity (Abstract)**  
  Defines common attributes (`id`, `name`) and the abstract method `show_info()`.

- **Customer**  
  Inherits from `BaseEntity`. Handles client data validation.

- **Service (Abstract)**  
  Inherits from `BaseEntity`. Defines base price and abstract `calculate_cost()` method.  
  **Subclasses:**
  - `RoomService`
  - `CleaningService`
  - `SpaService`
  - `RentedService`
  - `ConsultationService`  
  Each implements polymorphism by defining how to calculate costs based on days, hours, or quantity.

- **Reservation**  
  Associates a `Customer` with a `Service`. Handles date validations, statuses, and cost calculations (demonstrating method overloading via default arguments).

- **Exceptions (`exceptions.py`)**  
  Defines a hierarchy of custom errors inheriting from `Exception`.

---

## 🚀 How to Run

### 🔧 Prerequisites
- Python **3.8+**
- Tkinter (included with standard Python installations)

### ▶️ Execution
1. Navigate to the project root directory.
2. Run the main application file:

   ```bash
   python Main.py

3. The GUI window will open.  
4. Select one of the three **Simulation Scenarios** and click **"Run Simulation"**:

   - **Scenario 1 (Mixed):** Tests a combination of valid and invalid data.  
   - **Scenario 2 (Validation Failures):** Inputs bad data formats, negative IDs, and reversed dates to trigger and demonstrate custom exceptions.  
   - **Scenario 3 (Perfect Execution):** A clean run with valid data to demonstrate correct flow.  

5. View the results, including caught exceptions and successful creations, in the embedded console text box.  
   Check the `logs` folder for the saved error log.

---

## 📚 Documentation
All Python files are fully documented using **standard Python docstrings (PEP 257)** in English, explaining:
- Purpose of classes  
- Methods  
- Parameters  
- Exceptions raised  

---

## 📌 Note
***Project developed for Phase 4 of the Programming program.***
