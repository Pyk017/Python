import sqlite3
from employee import Employee

conn = sqlite3.connect("employee2.db")

c = conn.cursor()

# c.execute("""CREATE TABLE employee(first_name text, last_name text, pay integer)""")

def insert_emp(emp):
    with conn:
        c.execute("INSERT INTO employee VALUES (:first, :last, :pay)", {'first': emp.first, 'last': emp.last, 'pay': emp.pay})

def get_emp_by_name(lastname):
    c.execute("SELECT * FROM  employee WHERE last_name=:last", {'last': lastname})
    return c.fetchall()

def update_pay(emp, pay):
    with conn:
        c.execute("""UPDATE employee SET pay = :pay
                    WHERE first_name = :first AND last_name = :last""",
                    {'first': emp.first, 'last': emp.last, 'pay': pay})

def remove_emp(emp):
    with conn:
        c.execute("DELETE FROM employee WHERE first_name = :first AND last_name = :last",
        {'first': emp.first, 'last': emp.last})


emp_1 = Employee("Prakhar", "Kumar", "50000")
emp_2 = Employee("Yush", "Kumar", "60000")
emp_3 = Employee("Joe", "Doe", "70000")
emp_4 = Employee("Jane", "Doe", "80000")

insert_emp(emp_1)
insert_emp(emp_2)
insert_emp(emp_3)
insert_emp(emp_4)

emps = get_emp_by_name('Kumar')
print(emps)

conn.close()