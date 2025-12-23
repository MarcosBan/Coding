import csv
import os

fieldnames = ['id', 'date', 'description', 'amount']

def create_file():
    if not os.path.exists('expenses.csv'):
        with open('expenses.csv', 'w') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
        csv_file.close()

def register_create(description, amount, date):
    create_file()
    with open('expenses.csv', 'a') as csv_file:
        id = _count_file_rows()
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writerow({'id': id, 'date': date, 'description': description, 'amount': amount})
        return id
    csv_file.close()

def register_update(id, description, amount):
    temp_values = []
    print("In register update")
    with open('expenses.csv', 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            if row['id'] == id:
                row['description'] = description
                row['amount'] = amount
                temp_values.append(row)
            else:
                temp_values.append(row)
        with open('expenses.csv', 'w') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(temp_values)
    csv_file.close()

def register_delete(id):
    temp_values = []
    print("In register delete")
    with open('expenses.csv', 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            if row['id'] == id:
                continue
            else:
                temp_values.append(row)
                
        with open('expenses.csv', 'w') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(temp_values)
    csv_file.close()

def _count_file_rows():
    with open('expenses.csv', 'r') as csv_file:
        reader = csv.reader(csv_file)
        return len(list(reader))
    csv_file.close()

def list_expenses():
    with open('expenses.csv', 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        return list(reader)
    csv_file.close()