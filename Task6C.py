def write_employee_report(filename):
  employees = [
    {"name": "Alice", "department": "HR"},
    {"name": "Bob", "department": "Engineering"},
    {"name": "Charlie", "department": "Finance"}]
  with open("employee_report.txt", "w") as file:
    for employee in employees:
      line = f"Name: {employee['name']}, Department: {employee['department']}\n"
      file.write(line)
write_employee_report("employee_report.txt")
