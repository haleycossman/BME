import csv
with open("UpdatedMetaData.csv", newline="") as f:
    reader = csv.reader(f)
    header = next(reader)
    for h in headers:
        print(h)
        