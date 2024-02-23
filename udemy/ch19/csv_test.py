import csv

with open("file.csv", newline="", encoding="utf8") as f:
    csv_data = csv.reader(f)
    for row in csv_data:
        print(row[1].title())

# with open("new.csv", mode="w", newline="", encoding="utf8") as f:
#     csv_write = csv.writer(f, delimiter=",")
#     csv_write.writerows([["a", "b", "c"], ["d", "e", "f"]])