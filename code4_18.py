import math
from pathlib import Path


class Point:
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y

    def dis(self, point):
        return math.sqrt(
            (self.x - point.x) ** 2
            + (self.y - point.y) ** 2
        )


input_file = Path("data") / "points_4_18.txt"
output_file = Path("data") / "points_result_4_18.txt"

points = []

with input_file.open("r", encoding="utf-8") as file:
    header = file.readline().strip()
    if header.lower() != "point:":
        raise ValueError("Эхний мөр 'Point:' байх ёстой")

    for line in file:
        line = line.strip()
        if not line:
            continue

        # Жишээ: "4: 0, 500"
        name, coordinates = line.split(":", 1)
        x_text, y_text = coordinates.split(",", 1)
        points.append(Point(name.strip(), float(x_text), float(y_text)))

if len(points) < 2:
    raise ValueError("Зай тооцоход дор хаяж хоёр цэг шаардлагатай")

longest_distance = -1.0
first_point = None
second_point = None

for i in range(len(points) - 1):
    for j in range(i + 1, len(points)):
        distance = points[i].dis(points[j])

        if distance > longest_distance:
            longest_distance = distance
            first_point = points[i]
            second_point = points[j]

result = (
    f"Хамгийн хол цэгүүд: {first_point.name} "
    f"({first_point.x}, {first_point.y}) ба "
    f"{second_point.name} ({second_point.x}, {second_point.y})\n"
    f"Зай: {longest_distance:.6f}\n"
)

output_file.write_text(result, encoding="utf-8")
print(result)
print("Үр дүнгийн файл:", output_file.resolve())