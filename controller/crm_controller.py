from model.crm import crm
from view import terminal as view
from model import data_manager, util
import os


def list_customers():
    customers = data_manager.read_table_from_file(crm.DATAFILE)
    view.print_table(customers, crm.HEADERS)


def add_customer():
    customers = data_manager.read_table_from_file(crm.DATAFILE)
    labels = ["Name", "Email", "Subscribed"]
    data = view.get_inputs(labels)
    data.insert(0, util.generate_id())
    for index, value in enumerate(data):
        yes_strings = ["Yes", "yes", "YES"]
        no_strings = ["No", "no", "NO"]
        if value in yes_strings and value in data:
            data[index] = "1"
        elif value in no_strings and value in data:
            data[index] = "0"
    customers.append(data)
    data_manager.write_table_to_file(crm.DATAFILE, customers)


def update_customer():
    customers = data_manager.read_table_from_file(crm.DATAFILE)
    operation = None
    while operation != '0':
        print("What do you want to update?\n(1) Name\n(2) Email\n(3) Subscription status")
        operation = view.get_input("Select an operation")
        if operation == "1":
            customer_id = input("What is the ID of the customer you want to update? ")
            for customer in customers:
                if customer[0] == customer_id:
                    updated_name = input("What would the new name be? ")
                    customer[1] = updated_name
                    data_manager.write_table_to_file(crm.DATAFILE, customers)
            else:
                break
        elif operation == "2":
            customer_id = input("What is the ID of the customer you want to update? ")
            for customer in customers:
                if customer[0] == customer_id:
                    updated_name = input("What would the new email be? ")
                    customer[2] = updated_name
                    data_manager.write_table_to_file(crm.DATAFILE, customers)
            else:
                break
        elif operation == "3":
            customer_id = input("What is the ID of the customer you want to update? ")
            for customer in customers:
                if customer[0] == customer_id:
                    updated_name = input("What's the new status of the subscription'? ")
                    customer[3] = updated_name
                    data_manager.write_table_to_file(crm.DATAFILE, customers)
            else:
                break
        break
    else:
        update_customer()


def delete_customer():
    customers = data_manager.read_table_from_file(crm.DATAFILE)
    customer_id = input("What is the ID of the customer you want to delete? ")
    for customer in customers:
        if customer[0] == customer_id:
            customers = [customer_updated for customer_updated in customers if customer_updated[0] != customer_id]
            data_manager.write_table_to_file(crm.DATAFILE, customers)


def get_subscribed_emails():
    customers = data_manager.read_table_from_file(crm.DATAFILE)
    subscribed_customers = []
    label = "Emails for the subscribed customers"
    for customer in customers:
        if customer[3] == "1":
            subscribed_customers.append(customer[2])
    view.print_general_results(subscribed_customers, label)


def run_operation(option):
    if option == 1:
        list_customers()
    elif option == 2:
        add_customer()
    elif option == 3:
        update_customer()
    elif option == 4:
        delete_customer()
    elif option == 5:
        get_subscribed_emails()
    elif option == 0:
        return
    else:
        raise KeyError("There is no such option.")


def display_menu():
    options = ["Back to main menu",
               "List customers",
               "Add new customer",
               "Update customer",
               "Remove customer",
               "Subscribed customer emails"]
    view.print_menu("Customer Relationship Management", options)


def menu():
    os.system('cls')
    operation = None
    while operation != '0':
        display_menu()
        try:
            operation = view.get_input("Select an operation")
            run_operation(int(operation))
        except KeyError as err:
            view.print_error_message(err)
