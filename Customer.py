import exceptions 
from exceptions import *

class Customer:
    
    def __init__(self, customer_id, customer_name, email, phone):

        self.__customer_id = customer_id
        self.__customer_name = customer_name
        self.__email = email
        self.__phone = phone
    
        if not self.__customer_name.strip():
            raise exceptions.CustomerNameError("Customer name cannot be empty")
        if "@" not in self.__email:
            raise exceptions.EmailError("Invalid email format")
        if len(self.__phone) <= 7:
            raise exceptions.PhoneError("Phone cannot be less than 8 characters")
        if self.__customer_id <= 0:
            raise exceptions.CustomerIDError("Customer ID must be greater than 0")

    def get_name(self):
        return self.__customer_name
    
    def get_email(self):
        return self.__email
    
    def get_phone(self):
        return self.__phone
    
    def get_customer_id(self):
        return self.__customer_id

    def set_email(self, email):
        self.__email = email

    def set_phone(self, phone):
        self.__phone = phone
    
    
    def show_info(self):
        return f"Customer Name: {self.__customer_name}\nCustomer Email: {self.__email}\nCustomer Phone: {self.__phone}"
    
    def __str__(self):
        return self.show_info()
