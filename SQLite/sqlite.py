import sqlite3
from employee import Employee

conn = sqlite3.connect("employee.db")    # a connection object the represents our database
                                        # Now within this connect method we can either pass in a file where we want to store our data or we can even make 
                                        # an end memory database. In an in-memory database we'll have string here (":memory:").
                                        #  Here we are using a file.
                                        # So when we run that connect method it create that file even if it doesnot exit, if it exit then it just connects it.
                                        

c = conn.cursor()   # It is cursor which allows us to execute some sql commands so to create a cursor then we can just create a variable here.

# c.execute("""CREATE TABLE EMPLOYEE(
#             first_name text,
#             last_name text,
#             pay integer
#             )""")   # """ it is a docstring that allows us to write a string that's multiple lines without any special breaks.


# First we run it, It runs successfully. The second time we run it, it gives an error "OperationalError: table EMPLOYEE already exists"

# Now adding data to the database.

# c.execute("INSERT INTO employee VALUES('Yush', 'Kumar', '70000')")   # Inserting data into the database.

# Now checking that the data is being inserted in the database or not.

# c.execute("SELECT * FROM employee WHERE last_name='Kumar'") # Now  select statement provide some results that we can iterate through so to iterate
                        # through that qurey result then we can use a few different methods here like fetchone, fetchmany and fetchall.

                        # 1. fetchone = only returns the next row that satisfies the condition and if no more rows available then it just returns none.
                        # 2. fetchmany = This takes an argument of a number, it will return that number of rows as a list and if there are no more rows available then it will return empty list.
                        # 3. fetchall = it will returns the remaining rows that are left and return those as a list and if there are no more rows then it will return an empty list.

# print(c.fetchone())  # returns a tuple of ("Prakhar", "Kumar", "50000")
# print(c.fetchall())     # returns a list of tuple [("Prakhar", "Kumar", "50000")]



# Using Employee module created in employee.py file.

emp_1 = Employee('John', 'Doe', '80000')
emp_2 = Employee('Jane', 'Doe', '90000')


# c.execute("INSERT INTO employee VALUES('{}', '{}', '{}')".format(emp_1.first, emp_1.last, emp_1.pay)) # A bad way to of inserting as it is vulnerable to SQL injection attacks
                                            # There are two ways of doing it properly.
                                             

# 1. Instead of using regular brace placeholder, we can use question marks and this is a DB API placeholder and we also no longer need the quotes.
# c.execute("INSERT INTO employee VALUES(?, ?, ?)", (emp_1.first, emp_1.last, emp_1.pay))    # second argument of execute method contains the tuple of all data.

# conn.commit()
# # 2. Instead of there question marks, we are going to put a colon and a name describing the placeholder. like (:first, :last, :pay).
# # and the second argument of execute method contains the dictionary in which keys will be the placeholder (:first, :last, :pay) and values are the data of the employee.
# c.execute("INSERT INTO employee VALUES(:first, :last, :pay)", {'first': emp_2.first, 'last': emp_2.last, 'pay': emp_2.pay})

# conn.commit()


# c.execute("SELECT * FROM employee WHERE last_name=?", ('Doe',))     # for making second argument a tuple we have to use ',' after 'Doe', on using just a single value. 

print(c.fetchone())



# conn.commit()   # This commit the current transaction.

conn.close()    # Closing of connection.
