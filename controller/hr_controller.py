from model.hr import hr
from view import terminal as view
from model import data_manager, util
from datetime import datetime
import os


def list_employees():
    employees = data_manager.read_table_from_file(hr.DATAFILE)
    view.print_table(employees, hr.HEADERS)


def add_employee():
    employees = data_manager.read_table_from_file(hr.DATAFILE)
    labels = ["Name", "Date of birth", "Department", "Clearance"]
    print("'Date of birth' must be in ISO 8601 format (like 1989-03-21)")
    print("'Clearance' must be an integer from 0 (lowest) to 7 (highest)")
    data = view.get_inputs(labels)
    data.insert(0, util.generate_id())
    employees.append(data)
    data_manager.write_table_to_file(hr.DATAFILE, employees)


def update_employee():
    employees = data_manager.read_table_from_file(hr.DATAFILE)
    operation = None
    while operation != '0':
        print("What do you want to update?\n(1) Name\n(2) Date of Birth\n(3) Department\n(4) Clearance Level")
        operation = view.get_input("Select an operation")
        if operation == "1":
            employee_id = input("What is the ID of the employee you want to update? ")
            for employee in employees:
                if employee[0] == employee_id:
                    updated_name = input("What would the new name be? ")
                    employee[1] = updated_name
                    data_manager.write_table_to_file(hr.DATAFILE, employees)
            else:
                break
        elif operation == "2":
            employee_id = input("What is the ID of the employee you want to update? ")
            for employee in employees:
                if employee[0] == employee_id:
                    updated_name = input("What would the new date of birth be? ")
                    employee[2] = updated_name
                    data_manager.write_table_to_file(hr.DATAFILE, employees)
            else:
                break
        elif operation == "3":
            employee_id = input("What is the ID of the employee you want to update? ")
            for employee in employees:
                if employee[0] == employee_id:
                    updated_name = input("What's the new clearance level? ")
                    employee[3] = updated_name
                    data_manager.write_table_to_file(hr.DATAFILE, employees)
            else:
                break
        break
    else:
        update_employee()


def delete_employee():
    employees = data_manager.read_table_from_file(hr.DATAFILE)
    employee_id = input("What is the ID of the employee you want to delete? ")
    for employee in employees:
        if employee[0] == employee_id:
            employees = [employee_updated for employee_updated in employees if employee_updated[0] != employee_id]
            data_manager.write_table_to_file(hr.DATAFILE, employees)


def get_oldest_and_youngest():
    employees = data_manager.read_table_from_file(hr.DATAFILE)
    label1 = "The youngest employee is"
    label2 = "The oldest employee is"
    current_date = datetime.today().strftime('%Y-%m-%d')
    date_format = '%Y-%m-%d'
    year_index = 2
    list_of_ages = {}
    for employee in employees:
        employee_age = datetime.strptime(employee[year_index], date_format)
        today = datetime.strptime(current_date, date_format)
        difference = (today - employee_age).days
        list_of_ages[difference] = employee[1:-1]
    youngest_employee = list_of_ages[min(list_of_ages)]
    oldest_employee = list_of_ages[max(list_of_ages)]
    view.print_general_results(youngest_employee, label1)
    view.print_general_results(oldest_employee, label2)


def get_average_age():
    employees = data_manager.read_table_from_file(hr.DATAFILE)
    label = "The average age of employees is"
    current_date = datetime.today().strftime('%Y-%m-%d')
    date_format = '%Y-%m-%d'
    year_index = 2
    ages = []
    employee_count = 0
    for employee in employees:
        employee_age = datetime.strptime(employee[year_index], date_format)
        today = datetime.strptime(current_date, date_format)
        difference = (today - employee_age).days
        ages.append(difference)
        employee_count += 1
    average_age = int(((sum(ages) / employee_count) / 365))
    view.print_general_results(average_age, label)


def next_birthdays():
    employees = data_manager.read_table_from_file(hr.DATAFILE)
    label = "Employees with birthdays in the next 14 days are"
    date_format = '%Y-%m-%d'
    name_index = 1
    year_index = 2
    has_upcoming_birthday = []
    for employee in employees:
        employee_age = datetime.strptime(employee[year_index], date_format)
        if datetime.today().month == int(employee_age.month):
            if int(employee_age.day) - int(datetime.today().day) <= 14:
                has_upcoming_birthday.append(employee[name_index:])
    view.print_general_results(has_upcoming_birthday, label)


def count_employees_with_clearance():
    employees = data_manager.read_table_from_file(hr.DATAFILE)
    name_index = 1
    label = "This is the clearance breakdown"
    clearance_dict = {"0": [], "1": [], "2": [], "3": [], "4": [], "5": [], "6": [], "7": []}
    for employee in employees:
        for key in clearance_dict.keys():
            if key in employee:
                clearance_dict[key].append(employee[name_index])
    view.print_general_results(clearance_dict, label)


def count_employees_per_department():
    employees = data_manager.read_table_from_file(hr.DATAFILE)
    label = "This is the departments breakdown"
    name_index = 1
    department_index = 3
    departments_dict = {}
    for employee in employees:
        departments_dict.update({employee[department_index]: []})
    for employee in employees:
        for key in departments_dict.keys():
            if key in employee:
                departments_dict[key].append(employee[name_index])
    view.print_general_results(departments_dict, label)


def run_operation(option):
    if option == 1:
        list_employees()
    elif option == 2:
        add_employee()
    elif option == 3:
        update_employee()
    elif option == 4:
        delete_employee()
    elif option == 5:
        get_oldest_and_youngest()
    elif option == 6:
        get_average_age()
    elif option == 7:
        next_birthdays()
    elif option == 8:
        count_employees_with_clearance()
    elif option == 9:
        count_employees_per_department()
    elif option == 0:
        return
    else:
        raise KeyError("There is no such option.")


def display_menu():
    options = ["Back to main menu",
               "List employees",
               "Add new employee",
               "Update employee",
               "Remove employee",
               "Oldest and youngest employees",
               "Employees average age",
               "Employees with birthdays in the next two weeks",
               "Employees with clearance level",
               "Employee numbers by department"]
    view.print_menu("Human resources", options)


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
