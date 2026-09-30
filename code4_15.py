from pathlib import Path

data_dir = Path("data")
data_dir.mkdir(exist_ok=True)

file_path = data_dir / "points.txt"

with open(file_path, "w", encoding="utf-8") as f:
    f.write("point:\n")
    f.write("p1: 1.0, 1.0\n")
    f.write("p2: 2.0, 2.0\n")

print("Файл үүссэн:", file_path.resolve())