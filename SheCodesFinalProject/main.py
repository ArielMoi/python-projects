import utilities

print("hello, welcome to the employees track system.")

base_file_path = input('as a start, please type the file location to divert the data to - ')

try:
    with open(base_file_path + r'\employees.txt', 'a') as employees_file:
        None
except FileNotFoundError:
    print("the file wasn't found. make sure you describe the right path. type again: ")
    base_file_path = input('as a start, please type the file location to divert the data to - ')

print('GREAT. lets start.')
print("""
to add employee manually press 1
to add employee from file press 2
to delete employee manually press 3
to delete employee from file press 4
to mark attendance press 5
to generate attendance report for an employee press 6
to print report of current month for all employees press 7
to print a report for current month for all employees press 8
to print an attendance report of all the late employees who arrived after 09:30 press 9
to Exit the system press 10
""")

user_choise = 0
while user_choise != '10':
    user_choise = input('\n\nchoose what action you would like to take: ')
    if not user_choise.isdigit() or int(user_choise) > 10:
        print('you chose a number bigger the 10 or didnt type a number at all. please try again')
        continue

    if user_choise == '1':
        employee_name = input('type the employees name: ')
        employee_id = input('type the employees id: ')
        employee_phone = input('type the employee phone number: ')
        employee_age = input('type the employee age: ')
        for char in list(employee_name):
            if char == ' ':
                space_index = list(employee_name).index(' ')
                employee_name = employee_name[:space_index - 1] + '_' + employee_name[space_index + 1:]
        # id, name, phone, age == class __init__ format (and in file format)

        employee_name = utilities.Employee(employee_id, employee_name, employee_phone, employee_age)
        employee_name.add_employee(base_file_path)
        print('Done.')

    if user_choise == '2':
        file_path = input('please type the file path to the employees document you like to add: ')
        utilities.add_employee_from_file(file_path, base_file_path)

    if user_choise == '3':
        utilities.delete_employee(base_file_path)

    if user_choise == '4':
        utilities.delete_employees_from_file(base_file_path)

    if user_choise == '5':
        utilities.mark_attendance()

    if user_choise == '6':
        utilities.attendance_report()

    if user_choise == '7':
        employees_id = input('attendance report for a the employee(write id): ')
        month_to_report = input('choose the month to pull from: ')
        utilities.attendance_report_per_month(employees_id, month_to_report)

    if user_choise == '8':
        utilities.attendance_report_for_current_month()

    if user_choise == '9':
        utilities.report_late_employees()
