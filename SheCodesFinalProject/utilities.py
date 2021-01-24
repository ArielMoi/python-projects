# module for SheCodes final project
from datetime import datetime
# temporary file path for checking
base_file_path = r"C:\Users\Ariel\Documents\Python Scripts\SheCodesFinalProject\\"


class Employee:

    def __init__(self, id, name, phone, age):
        self._name = name
        self._phone = phone
        self._age = age
        self._id = id

    def add_employee(self, base_file_path):
        try:
            with open(base_file_path + r'\employees.txt', 'a') as employees_file:
                employees_file.writelines('{},{},{},{}\n'.format(self._id, self._name, self._phone, self._age))
        except FileNotFoundError:
            print("the file wasn't found. make sure you describe the right path.")
        else:
            format_str = '00/00/00,00.00'
            with open(base_file_path + r'\attendance_log.txt', 'a') as attendance_log:
                attendance_log.write('{},{}\n'.format(self._id, format_str))




#functions outside the class
def add_employee_from_file(file_path, base_file_path):
    # makes a list with all the employees. format = id, name, phone, age
    try:
        with open(file_path, 'r') as employees:
            list_all_employees_from_user_file = employees.readlines()
    except FileNotFoundError:
        print("the file wasn't found. make sure you describe the right path.")
    else:
        employees_userlist = []
        for employee in list_all_employees_from_user_file:
            employees_userlist.append(employee.split(','))

        for line in employees_userlist:
            with open(base_file_path + r'\\employees.txt',
                      'a') as employees_from_user_file:
                employees_from_user_file.write('{}, {}, {}, {}\n'.format(line[0], line[1], line[2], line[3][:-1]))


def delete_employee(base_file_path):
    try:
        with open(base_file_path + r'\\employees.txt', 'r+') as employees_file:
            employees_temp_list = employees_file.readlines()
            employees_list = [employee.split(',') for employee in employees_temp_list]
    except FileNotFoundError:
        print("the file wasn't found. make sure you describe the right path.")

    else:
        # letting the user choose the employee by id (to prevent mistakes because of repeated names)
        user_choice_for_employee = input('please type the id of the employee you would like to delete: ')
        employees_list_without_employee = []
        for employee in employees_list:
            if employee[0] != user_choice_for_employee:
                employees_list_without_employee.append(employee)

    # opens file again as w to write the employee list anew without the deleted employee
    try:
        with open(base_file_path + r'\\employees.txt', 'w') as employees_file:
            for employee in employees_list_without_employee:
                employees_file.writelines('{},{},{},{}'.format(employee[0], employee[1], employee[2], employee[3]))
    except FileNotFoundError:
        print("the file wasn't found. make sure you describe the right path.")


def delete_employees_from_file(base_file_path):
    file_to_delete_from = input('please write the file location to delete from: ')
    employees_to_delete_ids = []

    # gathering the ids from the file for employees to delete.
    try:
        with open(file_to_delete_from, 'r') as employees_to_delete_file:
            employees_to_delete = employees_to_delete_file.readlines()

            for employee in employees_to_delete:
                employee_as_list = employee.split(',')
                employees_to_delete_ids.append(employee_as_list[0])
    except FileNotFoundError:
        print("the file wasn't found. make sure you describe the right path.")

    # making a list for the employees regular list so to match between them later.
    try:
        with open(base_file_path + r'\\employees.txt', 'r+') as employees_file:
            employees_temp_list = employees_file.readlines()
            employees_list = [employee.split(',') for employee in employees_temp_list]
    except FileNotFoundError:
        print("the file wasn't found. make sure you describe the right path.")
    else:
        employees_new_list = []

        # compare ids from old list of employee to the list of employees to delete
        for employee in employees_list:
            if employee[0] not in employees_to_delete_ids:
                employees_new_list.append(employee)

        # adding only the undeleted employees to the employee file a new
        with open(base_file_path + r'\\employees.txt', 'w') as employees_file:
            for employee in employees_new_list:
                employees_file.writelines('{},{},{},{}'.format(employee[0], employee[1], employee[2], employee[3]))


def mark_attendance():
    employees_to_mark_id = input('please type the id of the employee to mark attendance: ')
    now = datetime.now()
    with open(base_file_path + r'\\attendance_log.txt', 'r+') as attendance_file:
        attendance_list = attendance_file.read().split('\n')

        #checking to find employee
        checking = 0
        for line in attendance_list:
            if line.startswith(str(employees_to_mark_id)):
                checking +=1
        if checking <= 0:
            print("didn't find the id. please try again")


        # making a new list with the new attendance data
        temp_list = []
        for line in attendance_list:
            if line.startswith(str(employees_to_mark_id)):
                line = line + now.strftime(",%d/%m/%y,%H.%M")
            temp_list.append(line)
    with open(base_file_path + r'\\attendance_log.txt', 'w') as attendance_file:
        for line in temp_list:
            attendance_file.write(line +'\n')


def attendance_report():
    employees_id = input('attendance report for a the employee(write id): ')
    with open(base_file_path + r'\\attendance_log.txt', 'r+') as attendance_file:
        attendance_list = attendance_file.read().split('\n')
        for line in attendance_list:
            if line.startswith(str(employees_id)):
                employee_attendance_report = line[6:]


        #checking to find employee
        checking = 0
        for line in attendance_list:
            if line.startswith(str(employees_id)):
                checking +=1
        if checking <= 0:
            print("didn't find the id. please try again")


        #creating an int var to check every second iteration so it will print more nicely
        random_num = 1

        for datetime in employee_attendance_report.split(','):
            random_num +=1
            if random_num % 2 != 0:
                print(datetime+'\n')
            else:
                print(datetime)


def attendance_report_per_month(employees_id, month_to_report):
    employee_attendance_report = ''
    with open(base_file_path + r'\\attendance_log.txt', 'r+') as attendance_file:
        attendance_list = attendance_file.read().split('\n')
        for line in attendance_list:
            if line.startswith(str(employees_id)):
                employee_attendance_report = line[6:]

        employee_attendance_report = employee_attendance_report.split(',')
        for datetime in employee_attendance_report:
            #adding 2 to prevent DivideByZeroError
            if (employee_attendance_report.index(datetime) + 2) % 2 == 0:
                if datetime[3:5] == month_to_report:
                    print(datetime + ' ' + employee_attendance_report[employee_attendance_report.index(datetime) + 1])


def attendance_report_for_current_month():
    now = datetime.now()
    current_month = now.strftime('%m')
    with open(base_file_path + r'\\employees.txt', 'r') as employees_file:
        employees_list = employees_file.read().strip().split('\n')

        for employee in employees_list:
            print('employee ' + employee.split(',')[1] + ' id:' + employee.split(',')[0] + ' current month report:')
            attendance_report_per_month(employee[0:5], current_month)



def report_late_employees():
    with open(base_file_path + r'\\employees.txt', 'r') as employees_file:
        employees_list = employees_file.read().strip().split('\n')

    with open(base_file_path + r'\\attendance_log.txt', 'r') as attendance_log_file:
        attendance_log = attendance_log_file.read().strip().split('\n')

    #making a dict attendance log
    attendance_log_dict = {}
    for line in attendance_log:
        ######attendance_log_dict[line[0:5]] = line[6:]
        attendance_log_dict[line[0:5]] = '[' + line[6:] + ']'


    late_employees_list = []
    for key, value in attendance_log_dict.items():
        value = value.split(',')
        for val in value:
            if '/' in val or val == '.':
                continue

            else:
                val = val[:-1] if ']' in val else val

                #divide the late times
                if float(val) > 09.30:
                    late_employees_list.append((key, val))

    #comparing the late times to the employees to reference it to the right employee
    for tuple in late_employees_list:
        for employee in employees_list:
            employee = employee.split(',')

            if tuple[0] == employee[0]:
                for line in attendance_log:
                    line = line.split(',')
                    if line[0] == tuple[0]:
                        print('the employee ', employee[0], employee[1], 'was late at: ')
                        date_index = line.index(tuple[1]) - 1
                        print(line[date_index], tuple[1])
