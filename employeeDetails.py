num = int(input("Enter the number of employees: "))
employees = {}
for i in range(num):
    name = input(f"Enter the name of the {i+1}st employee: " )
    salary = input(f"Enter the salary of {i+1}st employee: ")
    employees[name] = salary
print(employees)
while True:
    name = input("Enter the name of the employee: ")
    salary = employees.get(name, -1)
    if salary == -1:
        print("The employee doesnot exist.")
    else:
        print("Salary of the employee is ",salary)
    choice = input("Do you want to continue: Yes|No ")
    if choice == 'No' or 'no':
        break