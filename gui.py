import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import sys
import threading
import logging
import datetime
from models.Customer import Customer
from models.Service import (
    RoomService, SpaService, CleaningService, 
    RentedService, ConsultationService, 
    CustomDailyService, CustomHourlyService
)
from models.Reservation import Reservation

class PrintLogger:
    """
    A helper class used to intercept standard system output (sys.stdout).
    Redirects print() statements to a Tkinter ScrolledText widget for UI monitoring.
    """
    def __init__(self, text_widget):
        self.text_widget = text_widget

    def write(self, message):
        """Writes the message into the Tkinter text widget and auto-scrolls."""
        self.text_widget.insert(tk.END, message)
        self.text_widget.see(tk.END)
        self.text_widget.update_idletasks()

    def flush(self):
        """Required flush method for file-like objects (no-op in this context)."""
        pass

class SoftwareFJ_GUI:
    """
    Main Graphical User Interface (GUI) class for the Software FJ Integral System.
    Handles UI rendering, user interaction, dynamic forms, and error interception.
    """
    
    def __init__(self, root, run_simulation_callback):
        """
        Initializes the GUI, defines local state lists, and sets up the views.

        Args:
            root (tk.Tk): The root Tkinter window instance.
            run_simulation_callback (function): A reference to the simulation function defined in Main.py.
        """
        self.root = root
        self.root.title("Software FJ - Integral System")
        self.root.geometry("900x700")
        self.run_simulation_callback = run_simulation_callback

        # Memory storage for manual inputs
        self.manual_customers = []
        self.manual_services = []
        self.manual_reservations = []

        self.setup_ui()
        # Redirect console output to the UI text widget
        sys.stdout = PrintLogger(self.console_output)

    def setup_ui(self):
        """Initializes the main notebook (tabbed interface) and adds core tabs."""
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(expand=True, fill='both', padx=10, pady=10)

        self.tab_simulations = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_simulations, text='Automated Simulations')
        
        self.tab_manual = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_manual, text='Manual Entry')
        
        self.setup_simulations_tab()
        self.setup_manual_tab()

    def setup_simulations_tab(self):
        """Constructs the layout, radio buttons, and console widget for the Simulations tab."""
        frame_controls = ttk.Frame(self.tab_simulations)
        frame_controls.pack(fill='x', padx=10, pady=10)

        ttk.Label(frame_controls, text="Select a scenario:").pack(side=tk.LEFT, padx=5)

        self.sim_var = tk.StringVar(value="sim1")
        ttk.Radiobutton(frame_controls, text="1: Mixed Errors", variable=self.sim_var, value="sim1").pack(side=tk.LEFT, padx=5)
        ttk.Radiobutton(frame_controls, text="2: Validation Failures", variable=self.sim_var, value="sim2").pack(side=tk.LEFT, padx=5)
        ttk.Radiobutton(frame_controls, text="3: Perfect Run", variable=self.sim_var, value="sim3").pack(side=tk.LEFT, padx=5)

        ttk.Button(frame_controls, text="Run Simulation", command=self.run_simulation_thread).pack(side=tk.RIGHT, padx=5)
        ttk.Button(frame_controls, text="Clear Console", command=self.clear_console).pack(side=tk.RIGHT, padx=5)

        frame_console = ttk.LabelFrame(self.tab_simulations, text="System Logs & Output")
        frame_console.pack(expand=True, fill='both', padx=10, pady=10)

        self.console_output = scrolledtext.ScrolledText(frame_console, wrap=tk.WORD, font=("Consolas", 10))
        self.console_output.pack(expand=True, fill='both', padx=5, pady=5)

    def setup_manual_tab(self):
        """Constructs the complex layout for manual registrations (Customers, Services, Reservations)."""
        self.tab_manual.columnconfigure(0, weight=1)
        self.tab_manual.columnconfigure(1, weight=1)

        # --- Customer Form ---
        frame_cust = ttk.LabelFrame(self.tab_manual, text="1. Register Customer")
        frame_cust.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        
        ttk.Label(frame_cust, text="ID:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.c_id_entry = ttk.Entry(frame_cust)
        self.c_id_entry.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(frame_cust, text="Name:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.c_name_entry = ttk.Entry(frame_cust)
        self.c_name_entry.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(frame_cust, text="Email:").grid(row=2, column=0, padx=5, pady=5, sticky="e")
        self.c_email_entry = ttk.Entry(frame_cust)
        self.c_email_entry.grid(row=2, column=1, padx=5, pady=5)

        ttk.Label(frame_cust, text="Phone:").grid(row=3, column=0, padx=5, pady=5, sticky="e")
        self.c_phone_entry = ttk.Entry(frame_cust)
        self.c_phone_entry.grid(row=3, column=1, padx=5, pady=5)

        ttk.Button(frame_cust, text="Create Customer", command=self.add_manual_customer).grid(row=4, column=0, columnspan=2, pady=10)

        # --- Service Form ---
        frame_serv = ttk.LabelFrame(self.tab_manual, text="2. Register Service")
        frame_serv.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

        ttk.Label(frame_serv, text="ID:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.s_id_entry = ttk.Entry(frame_serv)
        self.s_id_entry.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(frame_serv, text="Name:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.s_name_entry = ttk.Entry(frame_serv)
        self.s_name_entry.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(frame_serv, text="Price/Rate:").grid(row=2, column=0, padx=5, pady=5, sticky="e")
        self.s_price_entry = ttk.Entry(frame_serv)
        self.s_price_entry.grid(row=2, column=1, padx=5, pady=5)

        ttk.Label(frame_serv, text="Type:").grid(row=3, column=0, padx=5, pady=5, sticky="e")
        self.s_type_cb = ttk.Combobox(frame_serv, values=["Room", "Spa", "Cleaning", "Rental", "Consultation", "Custom..."], state="readonly")
        self.s_type_cb.current(0)
        self.s_type_cb.grid(row=3, column=1, padx=5, pady=5)
        self.s_type_cb.bind("<<ComboboxSelected>>", self.on_service_type_change)

        # Dynamic Billing Mode field (hidden by default)
        self.lbl_billing = ttk.Label(frame_serv, text="Billing Mode:")
        self.s_billing_mode_cb = ttk.Combobox(frame_serv, values=["Days", "Hours"], state="readonly")
        self.s_billing_mode_cb.current(0)

        ttk.Button(frame_serv, text="Create Service", command=self.add_manual_service).grid(row=5, column=0, columnspan=2, pady=10)

        # --- Reservation Form (Dynamic Labels) ---
        frame_res = ttk.LabelFrame(self.tab_manual, text="3. Create & Confirm Reservation")
        frame_res.grid(row=0, column=1, rowspan=2, padx=10, pady=10, sticky="nsew")

        # StringVars to update label text dynamically
        self.lbl_res_date_var = tk.StringVar(value="Start Date (YYYY-MM-DD):")
        self.lbl_res_time_var = tk.StringVar(value="Start Time (HH:MM):")
        self.lbl_res_qty_var = tk.StringVar(value="Duration:")

        ttk.Label(frame_res, text="Res. ID:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.r_id_entry = ttk.Entry(frame_res)
        self.r_id_entry.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(frame_res, text="Customer:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.r_cust_cb = ttk.Combobox(frame_res, state="readonly")
        self.r_cust_cb.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(frame_res, text="Service:").grid(row=2, column=0, padx=5, pady=5, sticky="e")
        self.r_serv_cb = ttk.Combobox(frame_res, state="readonly")
        self.r_serv_cb.grid(row=2, column=1, padx=5, pady=5)
        self.r_serv_cb.bind("<<ComboboxSelected>>", self.on_res_service_selected)

        ttk.Label(frame_res, textvariable=self.lbl_res_date_var).grid(row=3, column=0, padx=5, pady=5, sticky="e")
        self.r_in_entry = ttk.Entry(frame_res)
        self.r_in_entry.grid(row=3, column=1, padx=5, pady=5)
        
        ttk.Label(frame_res, textvariable=self.lbl_res_time_var).grid(row=4, column=0, padx=5, pady=5, sticky="e")
        self.r_time_entry = ttk.Entry(frame_res)
        self.r_time_entry.insert(0, "12:00") # Default fallback time
        self.r_time_entry.grid(row=4, column=1, padx=5, pady=5)

        ttk.Label(frame_res, textvariable=self.lbl_res_qty_var).grid(row=5, column=0, padx=5, pady=5, sticky="e")
        self.r_qty_entry = ttk.Entry(frame_res)
        self.r_qty_entry.grid(row=5, column=1, padx=5, pady=5)

        ttk.Button(frame_res, text="Calculate Check-Out & Confirm", command=self.add_manual_reservation).grid(row=6, column=0, columnspan=2, pady=15)
        
        ttk.Label(frame_res, text="* Output logs will appear in the Console tab.", justify=tk.CENTER, foreground="gray").grid(row=7, column=0, columnspan=2, pady=5)

    def on_service_type_change(self, event):
        """
        Event Handler: Triggered when the Service Type combobox selection changes.
        Dynamically renders the "Billing Mode" combobox ONLY if "Custom..." is selected.
        
        Args:
            event: The UI event triggered by Tkinter.
        """
        if self.s_type_cb.get() == "Custom...":
            self.lbl_billing.grid(row=4, column=0, padx=5, pady=5, sticky="e")
            self.s_billing_mode_cb.grid(row=4, column=1, padx=5, pady=5)
        else:
            self.lbl_billing.grid_remove()
            self.s_billing_mode_cb.grid_remove()

    def on_res_service_selected(self, event=None):
        """
        Event Handler: Triggered when a Service is selected in the Reservation form.
        Reads the billing strategy of the selected Service object (days or hours) 
        and updates the UI Labels dynamically to guide the user inputs.
        
        Args:
            event: The UI event triggered by Tkinter (optional).
        """
        idx = self.r_serv_cb.current()
        if idx == -1: return
        
        srv = self.manual_services[idx]
        if srv.get_billing_type() == 'days':
            self.lbl_res_date_var.set("Check-in Date (YYYY-MM-DD):")
            self.lbl_res_time_var.set("Check-in Time (HH:MM):")
            self.lbl_res_qty_var.set("Duration (Days):")
        else:
            self.lbl_res_date_var.set("Reservation Date (YYYY-MM-DD):")
            self.lbl_res_time_var.set("Reservation Time (HH:MM):")
            self.lbl_res_qty_var.set("Duration (Hours):")

    def update_dropdowns(self):
        """
        Helper method to re-populate the UI Comboboxes whenever a new 
        Customer or Service is successfully registered.
        """
        cust_names = [f"{c.get_customer_id()} - {c.get_name()}" for c in self.manual_customers]
        self.r_cust_cb['values'] = cust_names
        if cust_names and self.r_cust_cb.get() == "": 
            self.r_cust_cb.current(0)

        serv_names = [f"{s.get_service_id()} - {s.get_service_name()} ({s.get_billing_type()})" for s in self.manual_services]
        self.r_serv_cb['values'] = serv_names
        if serv_names and self.r_serv_cb.get() == "": 
            self.r_serv_cb.current(0)
            self.on_res_service_selected() # Trigger label update

    def add_manual_customer(self):
        """
        Reads user input, attempts to instantiate a new Customer object,
        and gracefully intercepts Validation exceptions via a try/except block.
        """
        try:
            c_id = int(self.c_id_entry.get())
            name = self.c_name_entry.get()
            email = self.c_email_entry.get()
            phone = self.c_phone_entry.get()
            
            new_cust = Customer(c_id, name, email, phone)
            self.manual_customers.append(new_cust)
            self.update_dropdowns()
            
            messagebox.showinfo("Success", f"Customer '{name}' registered!")
            print(f"[MANUAL SUCCESS] Registered Customer: {name}")
            
            # Clear fields
            for entry in (self.c_id_entry, self.c_name_entry, self.c_email_entry, self.c_phone_entry):
                entry.delete(0, tk.END)

        except Exception as e:
            messagebox.showerror("Error", str(e))

    def add_manual_service(self):
        """
        Reads user input, applies polymorphism to instantiate the correct Service subclass
        based on user selection, and handles errors via try/except.
        """
        try:
            s_id = int(self.s_id_entry.get())
            name = self.s_name_entry.get()
            price = float(self.s_price_entry.get())
            s_type = self.s_type_cb.get()

            # Dynamic Polymorphism
            if s_type == "Room":
                new_serv = RoomService(s_id, name, price)
            elif s_type == "Spa":
                new_serv = SpaService(s_id, name, price)
            elif s_type == "Cleaning":
                new_serv = CleaningService(s_id, name, price)
            elif s_type == "Rental":
                new_serv = RentedService(s_id, name, price)
            elif s_type == "Consultation":
                new_serv = ConsultationService(s_id, name, price)
            else: # Custom...
                mode = self.s_billing_mode_cb.get()
                if mode == "Days":
                    new_serv = CustomDailyService(s_id, name, price)
                else:
                    new_serv = CustomHourlyService(s_id, name, price)

            self.manual_services.append(new_serv)
            self.update_dropdowns()
            
            messagebox.showinfo("Success", f"Service '{name}' registered!")
            print(f"[MANUAL SUCCESS] Registered Service: {name} ({new_serv.get_billing_type()})")

            for entry in (self.s_id_entry, self.s_name_entry, self.s_price_entry):
                entry.delete(0, tk.END)

        except Exception as e:
            messagebox.showerror("Error", str(e))

    def add_manual_reservation(self):
        """
        Validates the Reservation form. 
        Automatically calculates the End/Check-Out datetime based on the starting
        datetime and the requested duration, determining if the duration means 
        'hours' or 'days' depending on the associated Service object's billing policy.
        """
        try:
            r_id = int(self.r_id_entry.get())
            in_date = self.r_in_entry.get()
            in_time = self.r_time_entry.get()
            qty = int(self.r_qty_entry.get())

            cust_idx = self.r_cust_cb.current()
            serv_idx = self.r_serv_cb.current()

            if cust_idx == -1 or serv_idx == -1:
                messagebox.showerror("Error", "Create and select a Customer and Service first.")
                return

            selected_cust = self.manual_customers[cust_idx]
            selected_serv = self.manual_services[serv_idx]

            # Validate and Calculate Dates automatically using timedelta
            try:
                start_str = f"{in_date} {in_time}"
                start_dt = datetime.datetime.strptime(start_str, "%Y-%m-%d %H:%M")
            except ValueError:
                raise Exception("Invalid Date/Time format. Ensure YYYY-MM-DD and HH:MM.")

            if selected_serv.get_billing_type() == 'days':
                end_dt = start_dt + datetime.timedelta(days=qty)
            else:
                end_dt = start_dt + datetime.timedelta(hours=qty)

            end_str = end_dt.strftime("%Y-%m-%d %H:%M")

            # The Reservation class verifies the newly calculated end date
            new_res = Reservation(r_id, start_str, end_str, selected_cust, selected_serv, qty)
            new_res.confirm_reservation()
            self.manual_reservations.append(new_res)

            total_cost = new_res.calculate_total_cost()
            msg = (f"Reservation {r_id} confirmed!\n\n"
                   f"Start: {start_str}\n"
                   f"Calculated End: {end_str}\n"
                   f"Total Cost: ${total_cost}")
                   
            messagebox.showinfo("Success", msg)
            print(f"[MANUAL SUCCESS] Reservation {r_id} | End: {end_str} | Total: ${total_cost}")

            for entry in (self.r_id_entry, self.r_in_entry, self.r_qty_entry):
                entry.delete(0, tk.END)

        except Exception as e:
            messagebox.showerror("Error", str(e))

    def clear_console(self):
        """Clears all text currently printed in the log console."""
        self.console_output.delete('1.0', tk.END)

    def run_simulation_thread(self):
        """
        Spawns a new Python Thread to execute the automated simulation logic
        passed from Main.py. This prevents the Tkinter GUI from freezing 
        during execution.
        """
        scenario = self.sim_var.get()
        self.console_output.insert(tk.END, f"\n{'='*50}\nSTARTING {scenario.upper()}\n{'='*50}\n")
        thread = threading.Thread(target=self.run_simulation_callback, args=(scenario,))
        thread.start()
