import mysql.connector

mydb = mysql.connector.connect(
    host = 'o63bgj.h.filess.io',
    port = 3306,
    user = 'Subbu_arrangetax',
    password = '1260ca9a23574a8e7f3da444907b78541fd5f1a4',
    database = 'Subbu_arrangetax'
)

if mydb.is_connected():
    print("✅ Database has been connected successfully")
else:
    print("Connection was unsuccessfully")

cursor = mydb.cursor()

def add_employee():
    name = input("Enter Employee name :")
    department = input("Enter department name :")
    salary = int(input("Enter salary : "))

    cursor.execute("insert into employees(name, department, salary) values (%s,%s,%s)",(name, department,salary))

    mydb.commit()

    print(f"✅ Employee {name} has been successfully added")

def view_employees():
    cursor.execute("select id, name, department, salary from employees")
    records = cursor.fetchall()

    if not records:
        print("no employee are found")
        return

    print("=================================")

    total = 0
    for i, row in enumerate(records, start =1):
        emp_id, name, department,salary = row
        print(f"{i} {emp_id} | {name} | {department} | ₹{salary:,}")
        total += salary
    avg = total/len(records)
    print("=================================")
    print(f"Average Salary = ₹{round(avg,2):,}")    

def update_salary():
    emp_id = input("Enter Id of the employee :")
    new_salary = int(input("Enter the New salary :"))

    cursor.execute("update employees set salary = %s where id = %s",(new_salary,emp_id))
    mydb.commit()

    if cursor.rowcount == 0:
        print("No employee found on mentioned ID")
    else:
        print("✅ Salary has been updated Successfully")

def delete_employee():
    emp_id = input("Enter the ID of the employee to delete")

    cursor.execute("delete from employees where id = %s",(emp_id,))
    mydb.commit()

    if cursor.rowcount == 0:
        print("No records found to delete")
    else:
        print("✅ Successfully deleted the employee details")

def search_department():
    dept = input("Enter department name")

    cursor.execute("select id,name,department,salary from employees where department = %s",(dept,))
    records = cursor.fetchall()

    if not records:
        print("No records found of such department")
        return
    print("===================================")
    for row in records:
        emp_id,name,department,salary = row
        print(f"{emp_id} | {name} |{department} | ₹{salary:,}")        
while True:
    print("/n ===========Employee Management System================")
    print("1. Add employee")
    print("2. View All employees")
    print("3. update salary")
    print("4. Delete employee")
    print("5. Search by Department")
    print("6. Exit")
    print("==========================================================")

    choice = input("Enter your choice :")

    if choice == '1':
        add_employee()
    elif choice == '2':
        view_employees()
    elif choice =='3':
        update_salary()
    elif choice =='4':
        delete_employee()
    elif choice == '5':
        search_department()
    elif choice == '6':
        print("Closing connection.......")
        print("Exited Successfully")
        break
    else:
        print("Invalid Choice")










