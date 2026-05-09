import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import sys
import threading
import logging
from models.Customer import Customer
from models.Service import RoomService, SpaService, CleaningService, RentedService, ConsultationService
from models.Reservation import Reservation

class PrintLogger:
    """A helper class to redirect print statements to a Tkinter Text widget."""
    def __init__(self, text_widget):
        self.text_widget = text_widget

    def write(self, message):
        self.text_widget.insert(tk.END, message)
        self.text_widget.see(tk.END) # Auto-scroll
        self.text_widget.update_idletasks()

    def flush(self):
        pass

class SoftwareFJ_GUI:
    """Main GUI application class using tkinter."""
    
    def __init__(self, root, run_simulation_callback):
        self.root = root
        self.root.title("Software FJ - Integral System")
        self.root.geometry("900x700")
        self.run_simulation_callback = run_simulation_callback

        # Lists to hold manual data independently from simulations
        self.manual_customers = []
        self.manual_services = []
        self.manual_reservations = []

        self.setup_ui()
        
        # Redirect stdout to the console widget
        sys.stdout = PrintLogger(self.console_output)

    def setup_ui(self):
        """Sets up the GUI layout with tabs."""
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(expand=True, fill='both', padx=10, pady=10)

        # Tab 1: Simulations
        self.tab_simulations = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_simulations, text='Automated Simulations')
        
        # Tab 2: Manual Entry
        self.tab_manual = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_manual, text='Manual Entry')
        
        self.setup_simulations_tab()
        self.setup_manual_tab()

    def setup_simulations_tab(self):
        """Layout for the Automated Simulations tab."""
        frame_controls = ttk.Frame(self.tab_simulations)
        frame_controls.pack(fill='x', padx=10, pady=10)

        lbl_desc = ttk.Label(frame_controls, text="Select a simulation scenario to run:")
        lbl_desc.pack(side=tk.LEFT, padx=5)

        self.sim_var = tk.StringVar(value="sim1")
        
        r1 = ttk.Radiobutton(frame_controls, text="1: Mixed Errors", variable=self.sim_var, value="sim1")
        r2 = ttk.Radiobutton(frame_controls, text="2: Data Validation", variable=self.sim_var, value="sim2")
        r3 = ttk.Radiobutton(frame_controls, text="3: Perfect Run", variable=self.sim_var, value="sim3")
        
        r1.pack(side=tk.LEFT, padx=5)
        r2.pack(side=tk.LEFT, padx=5)
        r3.pack(side=tk.LEFT, padx=5)

        btn_run = ttk.Button(frame_controls, text="Run Simulation", command=self.run_simulation_thread)
        btn_run.pack(side=tk.RIGHT, padx=5)
        
        btn_clear = ttk.Button(frame_controls, text="Clear Console", command=self.clear_console)
        btn_clear.pack(side=tk.RIGHT, padx=5)

        # Console Output inside GUI
        frame_console = ttk.LabelFrame(self.tab_simulations, text="System Logs & Output")
        frame_console.pack(expand=True, fill='both', padx=10, pady=10)

        self.console_output = scrolledtext.ScrolledText(frame_console, wrap=tk.WORD, font=("Consolas", 10))
        self.console_output.pack(expand=True, fill='both', padx=5, pady=5)

    def setup_manual_tab(self):
        """Layout for the Manual Entry tab with forms."""
        self.tab_manual.columnconfigure(0, weight=1)
        self.tab_manual.columnconfigure(1, weight=1)

        # --- Customer Registration Form ---
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

        # --- Service Registration Form ---
        frame_serv = ttk.LabelFrame(self.tab_manual, text="2. Register Service")
        frame_serv.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

        ttk.Label(frame_serv, text="ID:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.s_id_entry = ttk.Entry(frame_serv)
        self.s_id_entry.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(frame_serv, text="Name:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.s_name_entry = ttk.Entry(frame_serv)
        self.s_name_entry.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(frame_serv, text="Price:").grid(row=2, column=0, padx=5, pady=5, sticky="e")
        self.s_price_entry = ttk.Entry(frame_serv)
        self.s_price_entry.grid(row=2, column=1, padx=5, pady=5)

        ttk.Label(frame_serv, text="Type:").grid(row=3, column=0, padx=5, pady=5, sticky="e")
        self.s_type_cb = ttk.Combobox(frame_serv, values=["Room", "Spa", "Cleaning", "Rental", "Consultation"], state="readonly")
        self.s_type_cb.current(0)
        self.s_type_cb.grid(row=3, column=1, padx=5, pady=5)

        ttk.Button(frame_serv, text="Create Service", command=self.add_manual_service).grid(row=4, column=0, columnspan=2, pady=10)

        # --- Reservation Creation Form ---
        frame_res = ttk.LabelFrame(self.tab_manual, text="3. Create & Confirm Reservation")
        frame_res.grid(row=0, column=1, rowspan=2, padx=10, pady=10, sticky="nsew")

        ttk.Label(frame_res, text="Res. ID:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.r_id_entry = ttk.Entry(frame_res)
        self.r_id_entry.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(frame_res, text="Customer:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.r_cust_cb = ttk.Combobox(frame_res, state="readonly")
        self.r_cust_cb.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(frame_res, text="Service:").grid(row=2, column=0, padx=5, pady=5, sticky="e")
        self.r_serv_cb = ttk.Combobox(frame_res, state="readonly")
        self.r_serv_cb.grid(row=2, column=1, padx=5, pady=5)

        ttk.Label(frame_res, text="Check-in (YYYY-MM-DD):").grid(row=3, column=0, padx=5, pady=5, sticky="e")
        self.r_in_entry = ttk.Entry(frame_res)
        self.r_in_entry.grid(row=3, column=1, padx=5, pady=5)

        ttk.Label(frame_res, text="Check-out (YYYY-MM-DD):").grid(row=4, column=0, padx=5, pady=5, sticky="e")
        self.r_out_entry = ttk.Entry(frame_res)
        self.r_out_entry.grid(row=4, column=1, padx=5, pady=5)

        ttk.Label(frame_res, text="Quantity/Days:").grid(row=5, column=0, padx=5, pady=5, sticky="e")
        self.r_qty_entry = ttk.Entry(frame_res)
        self.r_qty_entry.grid(row=5, column=1, padx=5, pady=5)

        ttk.Button(frame_res, text="Create & Confirm", command=self.add_manual_reservation).grid(row=6, column=0, columnspan=2, pady=15)
        
        ttk.Label(frame_res, text="* Logs for manual actions will appear\nin the 'Automated Simulations' console tab.", justify=tk.CENTER, foreground="gray").grid(row=7, column=0, columnspan=2, pady=5)

    def update_dropdowns(self):
        """Refreshes the comboboxes with current manual data."""
        cust_names = [f"{c.get_customer_id()} - {c.get_name()}" for c in self.manual_customers]
        self.r_cust_cb['values'] = cust_names
        if cust_names and self.r_cust_cb.get() == "": 
            self.r_cust_cb.current(0)

        serv_names = [f"{s.get_service_id()} - {s.get_service_name()}" for s in self.manual_services]
        self.r_serv_cb['values'] = serv_names
        if serv_names and self.r_serv_cb.get() == "": 
            self.r_serv_cb.current(0)

    def add_manual_customer(self):
        try:
            c_id = int(self.c_id_entry.get())
            name = self.c_name_entry.get()
            email = self.c_email_entry.get()
            phone = self.c_phone_entry.get()
            
            new_cust = Customer(c_id, name, email, phone)
            self.manual_customers.append(new_cust)
            self.update_dropdowns()
            
            messagebox.showinfo("Success", f"Customer '{name}' registered successfully!")
            print(f"[MANUAL SUCCESS] Registered Customer: {name}")
            
            for entry in (self.c_id_entry, self.c_name_entry, self.c_email_entry, self.c_phone_entry):
                entry.delete(0, tk.END)

        except ValueError:
            messagebox.showerror("Type Error", "Customer ID must be a valid whole number.")
        except Exception as e:
            logging.error(f"Manual Customer Error: {e}")
            messagebox.showerror("Validation Error", str(e))
            print(f"[MANUAL ERROR] Customer creation failed: {e}")

    def add_manual_service(self):
        try:
            s_id = int(self.s_id_entry.get())
            name = self.s_name_entry.get()
            price = float(self.s_price_entry.get())
            s_type = self.s_type_cb.get()

            if s_type == "Room":
                new_serv = RoomService(s_id, name, price)
            elif s_type == "Spa":
                new_serv = SpaService(s_id, name, price)
            elif s_type == "Cleaning":
                new_serv = CleaningService(s_id, name, price)
            elif s_type == "Rental":
                new_serv = RentedService(s_id, name, price)
            else:
                new_serv = ConsultationService(s_id, name, price)

            self.manual_services.append(new_serv)
            self.update_dropdowns()
            
            messagebox.showinfo("Success", f"Service '{name}' registered successfully!")
            print(f"[MANUAL SUCCESS] Registered Service: {name} ({s_type})")

            for entry in (self.s_id_entry, self.s_name_entry, self.s_price_entry):
                entry.delete(0, tk.END)

        except ValueError:
            messagebox.showerror("Type Error", "ID and Price must be valid numbers.")
        except Exception as e:
            logging.error(f"Manual Service Error: {e}")
            messagebox.showerror("Validation Error", str(e))
            print(f"[MANUAL ERROR] Service creation failed: {e}")

    def add_manual_reservation(self):
        try:
            r_id = int(self.r_id_entry.get())
            check_in = self.r_in_entry.get()
            check_out = self.r_out_entry.get()
            qty = int(self.r_qty_entry.get())

            cust_idx = self.r_cust_cb.current()
            serv_idx = self.r_serv_cb.current()

            if cust_idx == -1 or serv_idx == -1:
                messagebox.showerror("Selection Error", "Please create and select at least one Customer and one Service.")
                return

            selected_cust = self.manual_customers[cust_idx]
            selected_serv = self.manual_services[serv_idx]

            new_res = Reservation(r_id, check_in, check_out, selected_cust, selected_serv, qty)
            new_res.confirm_reservation()
            self.manual_reservations.append(new_res)

            total_cost = new_res.calculate_total_cost()
            messagebox.showinfo("Success", f"Reservation {r_id} confirmed!\nTotal Cost: ${total_cost}")
            print(f"[MANUAL SUCCESS] Confirmed Reservation ID: {r_id} | Total: ${total_cost}")

            for entry in (self.r_id_entry, self.r_in_entry, self.r_out_entry, self.r_qty_entry):
                entry.delete(0, tk.END)

        except ValueError:
            messagebox.showerror("Type Error", "Reservation ID and Quantity must be valid integers.")
        except Exception as e:
            logging.error(f"Manual Reservation Error: {e}")
            messagebox.showerror("Validation Error", str(e))
            print(f"[MANUAL ERROR] Reservation creation failed: {e}")

    def clear_console(self):
        """Clears the output text widget."""
        self.console_output.delete('1.0', tk.END)

    def run_simulation_thread(self):
        """Runs the simulation in a separate thread to prevent GUI freezing."""
        scenario = self.sim_var.get()
        self.console_output.insert(tk.END, f"\n{'='*50}\nSTARTING {scenario.upper()}\n{'='*50}\n")
        
        thread = threading.Thread(target=self.run_simulation_callback, args=(scenario,))
        thread.start()
