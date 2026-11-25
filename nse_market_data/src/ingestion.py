import csv
from pathlib import Path

project_dir = Path(__file__).resolve().parent.parent

file_path = project_dir / "data" / "Quote-Equity-AEROFLEX-EQ-25-11-2025-25-11-2026.csv"

with open(file_path, mode='r', newline="", encoding="utf-8-sig") as file:
    reader = csv.DictReader(file)

    print(reader.fieldnames)

    for index, row in enumerate(reader):
        if index == 5:
            break
        print(row)


# challenge 1 - First 10 records
with open(file_path, mode="r", newline="", encoding="utf-8-sig") as file:
    reader = csv.DictReader(file)

    for index, row in enumerate(reader):
        if index == 10:
            break

        print(row)
# challenge 2 - print only DATE, CLOSE and VOLUME fields for the first 5 record
with open(file_path, mode="r", newline="", encoding="utf-8-sig") as file:
    reader = csv.DictReader(file)

    for index, row in enumerate(reader):
        if index == 5:
            break
        print(row['DATE'], row['CLOSE'], row['VOLUME'])

# challenge 3 - Count total records
with open(file_path, mode="r", newline="", encoding="utf-8-sig") as file:
    reader = csv.DictReader(file)

    total_count = 0
    eq_count = 0
    for row in reader:
        if row['SERIES'] == 'EQ':
            eq_count += 1
        total_count += 1
    print("Total records:", total_count)
    print("EQ records:", eq_count)
    print(type(row["CLOSE"]))
    print(type(row["VOLUME"]))
                