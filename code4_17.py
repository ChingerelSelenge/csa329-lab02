from pathlib import Path

class Point:
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y


def readPointFile(fileName):
    points = []

    with open(fileName, "r", encoding="utf-8") as file:
        header = file.readline().strip()
        if header.lower() != "point:":
            raise ValueError("Эхний мөр 'point:' байх ёстой")

        for line in file:
            line = line.strip()
            if not line:
                continue

            _, coordinates = line.split(":", 1)
            x_text, y_text = coordinates.split(",", 1)

            point = Point(float(x_text), float(y_text))
            points.append(point)

    return points


points = readPointFile(Path("data") / "points.txt")

for point in points:
    print(point.x, point.y)