import json


with open('employees.json', 'r') as file:
    data = json.load(file)

language = data.get('programming_language')
employees = data.get('employees')

print(language)
print('- ' * 15)
for emp in employees:
    print(emp.get('id'), emp.get('fullname'))
