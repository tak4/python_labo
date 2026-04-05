import csv
import random

def create_test_csv(filename, num_rows=100):
    header = ['name', 'val1', 'val2', 'val3']
    data = [header]
    
    for i in range(1, num_rows + 1):
        row = [
            f'name_{i:03d}',
            random.randint(1, 100),
            random.randint(1, 100),
            random.randint(1, 100)
        ]
        data.append(row)
    
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerows(data)

if __name__ == "__main__":
    create_test_csv('test_data.csv')
    print("test_data.csv has been created.")
