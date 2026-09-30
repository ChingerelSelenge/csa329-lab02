from pathlib import Path

file_path = Path("data") / "points.txt"

with open(file_path, "r", encoding="utf-8") as f:
    print("1-р мөр:", repr(f.readline()))
    print("2-р мөр:", repr(f.readline()))
    print("3-р мөр:", repr(f.readline()))
    print("Файлын төгсгөл:", repr(f.readline()))

    f.seek(0)  # go to the begin of file
    print("Дахин эхний мөр:", repr(f.readline()))
    print("Үлдсэн мөрүүдийн жагсаалт:", f.readlines()) #read rest lines in a list

    f.seek(0)
    print("Бүх агуулга:")
    print(f.read()) #read rest lines as a string