import csv

# Відкриття CSV-файлу для читання
with open("data.csv", newline="") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        # print(', '.join(row))
        print(row)

with open("data.csv") as f:
    csv_data = csv.DictReader(f)

    print(csv_data)
    for row in csv_data:
        print(row)


# Дані для запису у CSV-файл
data = [
    ["Name", "Age", "City"],
    ["John", 30, "New York"],
    ["Alice", 25, "Los Angeles"],
    ["Bob", 35, "Chicago"],
]

# Відкриття CSV-файлу для запису
with open("output.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(data)

# Відкриття CSV-файлу для запису
with open("output2.csv", newline="") as csvfile:
    reader = csv.reader(csvfile, delimiter=";")
    for row in reader:
        print(row)
