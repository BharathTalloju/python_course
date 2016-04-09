__author__ = 'Kalyan'

max_marks = 25

problem_notes = '''
You are given a file containing organization data of company in the following format:

manager1 : employee1, employee2, employee3, ....

We will give you a data file, but for these problems you have to consider only the first N lines to simulate various
test cases instead of having multiple input files (ie) treat it is as if the file has only N lines

This represents a company with many organizations. Your job is to process the data into some format that
is usable for the following operations:

 1. Load the data given in first N lines of file into some python representation (you can write your own classes or
    reuse python builtin data structures). Lets call this employee_data. Note that the structure of the data you create
    should be based on the operations that you perform on it, so look at requirements 2 and 3 carefully and choose
    your structure accordingly.
 2. Given 2 employees e1 and e2, your task is to find the the first common manager (his name as string) of those two employees.
 3. Given the employee data, return the heads of organizations in the company (the heads of organizations don't report
    to anyone else).
 4. An employee can report to only one manager and you can assume the data is correct in this respect.

To avoid multiple file reads, we process the file data into some python object, keep it cached and reuse it for the
above operations multiple times.

Since we are not writing a command line tool, we won't take user input etc. here but you get the idea...
'''
import inspect
import os


# use the open_input_file routine given below to open the file in the same folder.
# raise ValueError if n <= 0
def load_data(file_name, n):
    f = open_input_file(file_name)
    data = []
    data.append(f.readline())
    data = [x.strip() for x in data]
    data = [x.split(':') for x in data]
    data = [[x[0].strip(),x[1].split(',')] for x in data]
    for line in data:
        line[1] = [x.strip() for x in line[1]]
    data = [[x[0],set(x[1])] for x in data]
    return data

    pass


# returns the name (str) of the first common manager (potentially including e1 or e2) or None if they are from
# different orgs or unknown employees.
def common_manager(e1, e2, employee_data):
    for line in employee_data:
        if e1.strip() in line[1] and e2.strip() in line[1]:
            return line[0]
    return None
    pass


# returns the set of organization heads in employee_data
# Note: you return a set of strings.
def org_heads(employee_data):
    managers = []
    employees = []

    for line in employee_data:
        managers.append(line[0])
        e = list(line[1])
        employees += e
    managers = set(managers)
    employees = set(employees)
    head = managers - employees
    return head
    pass

def open_input_file(file, mode="rt"):
    mod_dir = get_module_dir()
    test_file = os.path.join(mod_dir, file)
    return open(test_file, mode)


def get_module_dir():
    mod_file = inspect.getfile(inspect.currentframe())
    mod_dir = os.path.dirname(mod_file)
    return mod_dir


# write your own tests
def test_employee_queries():
    emp_data = load_data("employees.txt", 1)
    assert "Murthy" == common_manager("Patel", "Prem", emp_data)
    assert {"Murthy"} == org_heads(emp_data)

