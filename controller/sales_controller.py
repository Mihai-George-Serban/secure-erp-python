# from model.sales import sales
# from view import terminal as view
# from model import data_manager, util
# from datetime import datetime
# from datetimerange import DateTimeRange
# import os


# def list_transactions():
#     transactions = data_manager.read_table_from_file(sales.DATAFILE)
#     view.print_table(transactions, sales.HEADERS)


# def add_transaction():
#     transactions = data_manager.read_table_from_file(sales.DATAFILE)
#     labels = ["Product", "Price", "Date"]
#     data = view.get_inputs(labels)
#     new_customer = input("are you a new customer ? ")
#     if new_customer == "yes":
#         data.insert(0, util.generate_id())
#     elif new_customer == "no":
#         old_customer = input("what's your customer id ? ")
#         for transaction in transactions:
#             if old_customer in transaction:
#                 data.insert(0, old_customer)
#                 break
#     data.insert(0, util.generate_id())
#     transactions.append(data)
#     data_manager.write_table_to_file(sales.DATAFILE, transactions)


# def update_transaction():
#     transactions = data_manager.read_table_from_file(sales.DATAFILE)
#     operation = None
#     while operation != '0':
#         print("(1) Product\n(2) Price\n(3) Date")
#         operation = view.get_input("Select an operation")
#         if operation == "1":
#             transaction_id = input("What is the id of the transaction you want to update? ")
#             for transaction in transactions:
#                 if transaction[0] == transaction_id:
#                     updated_name = input("What would the new Product be? ")
#                     transaction[2] = updated_name
#                     data_manager.write_table_to_file(sales.DATAFILE, transactions)
#             else:
#                 break
#         elif operation == "2":
#             transaction_id = input("What is the id of the transaction you want to update? ")
#             for transaction in transactions:
#                 if transaction[0] == transaction_id:
#                     updated_name = input("What would the new Price be? ")
#                     transaction[3] = updated_name
#                     data_manager.write_table_to_file(sales.DATAFILE, transactions)
#             else:
#                 break
#         elif operation == "3":
#             transaction_id = input("What is the id of the transaction you want to update? ")
#             for transaction in transactions:
#                 if transaction[0] == transaction_id:
#                     updated_name = input("What would the date be? ")
#                     transaction[4] = updated_name
#                     data_manager.write_table_to_file(sales.DATAFILE, transactions)
#             else:
#                 break
#         break
#     else:
#         update_transaction()


# def delete_transaction():
#     transactions = data_manager.read_table_from_file(sales.DATAFILE)
#     transaction_id = input("What is the ID of the transaction you want to delete? ")
#     for transaction in transactions:
#         if transaction[0] == transaction_id:
#             transactions = [trnsct_updt for trnsct_updt in transactions if trnsct_updt[0] != transaction_id]
#             data_manager.write_table_to_file(sales.DATAFILE, transactions)


# def get_biggest_revenue_transaction():
#     prices = []
#     transactions = data_manager.read_table_from_file(sales.DATAFILE)
#     label = "Biggest revenue transaction is"
#     for transaction in transactions:
#         prices.append(float(transaction[3]))
#     max = prices[0]
#     for i in prices:
#         if max < i:
#             max = i
#     output = transactions[1]
#     view.print_general_results(output, label)


# def get_biggest_revenue_product():
#     prices = []
#     myDict = {}
#     transactions = data_manager.read_table_from_file(sales.DATAFILE)
#     label = "Biggest revenue product is"
#     for transaction in transactions:
#         if transaction[2] not in myDict:
#             myDict[transaction[2]] = float(transaction[3])
#         else:
#             myDict[transaction[2]] += float(transaction[3])
#     for x in myDict:
#         prices.append(myDict[x])
#     max = prices[0]
#     for i in prices:
#         if max < i:
#             max = i
#     for x in myDict:
#         if max == myDict[x]:
#             view.print_general_results(x, label)


# def count_transactions_between():
#     transactions = data_manager.read_table_from_file(sales.DATAFILE)
#     label = "The number of transactions between the given dates is"
#     dates = []
#     counter = 0
#     transaction_date1 = input("Type the first date:")
#     transaction_date2 = input("Type the second date:")
#     time_range = DateTimeRange(transaction_date1, transaction_date2)
#     for transaction in transactions:
#         date_dt = datetime.strptime(transaction[4], '%Y-%m-%d')
#         if date_dt in time_range:
#             dates.append(transaction)
#             counter += 1
#     view.print_general_results(counter, label)


# def sum_transactions_between():
#     transactions = data_manager.read_table_from_file(sales.DATAFILE)
#     label = "Sum of transactions between the given dates is"
#     sum = 0
#     transaction_date1 = input("Type the first date:")
#     transaction_date2 = input("Type the second date:")
#     time_range = DateTimeRange(transaction_date1, transaction_date2)
#     for transaction in transactions:
#         date_dt = datetime.strptime(transaction[4], '%Y-%m-%d')
#         if date_dt in time_range:
#             sum += float(transaction[3])
#     view.print_general_results(sum, label)


# def run_operation(option):
#     if option == 1:
#         list_transactions()
#     elif option == 2:
#         add_transaction()
#     elif option == 3:
#         update_transaction()
#     elif option == 4:
#         delete_transaction()
#     elif option == 5:
#         get_biggest_revenue_transaction()
#     elif option == 6:
#         get_biggest_revenue_product()
#     elif option == 7:
#         count_transactions_between()
#     elif option == 8:
#         sum_transactions_between()
#     elif option == 0:
#         return
#     else:
#         raise KeyError("There is no such option.")


# def display_menu():

#     options = ["Back to main menu",
#                "List transactions",
#                "Add new transaction",
#                "Update transaction",
#                "Remove transaction",
#                "Get the transaction that made the biggest revenue",
#                "Get the product that made the biggest revenue altogether",
#                "Count number of transactions between",
#                "Sum the price of transactions between"]
#     view.print_menu("Sales", options)


# def menu():
#     os.system('cls')
#     operation = None
#     while operation != '0':
#         display_menu()
#         try:
#             operation = view.get_input("Select an operation")
#             run_operation(int(operation))
#         except KeyError as err:
#             view.print_error_message(err)
