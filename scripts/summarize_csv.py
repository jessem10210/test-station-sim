import csv 

def summarize(path):
    columns = {"voltage": [], "temperature": [], "current": []}
    try:
        with open(path, newline="") as f:
            for row in csv.DictReader(f):
                for name in columns:
                    columns[name].append(float(row[name]))
    except FileNotFoundError:
        print(f"File not found: {path}")
        return

    for name, values in columns.items():
        print(f"{name}: min={min(values)}, max={max(values)}, mean={sum(values) / len(values):.2f}")

summarize("data/sample.csv")
