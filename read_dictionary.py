employee = {1: {'name': 'Sarah', 'age': '30', 'employee_status': 'active'},
          2: {'name': 'Tom', 'age': '45', 'employee_status': 'active'}}

for e_id, e_info in employee.items():
    print("\nEmployee ID:", e_id)

    for key in e_info:
        print(key + ':', e_info[key])