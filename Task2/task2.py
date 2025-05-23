import sys

def main():
    if len(sys.argv) != 3:
        print("Использование: python task2.py circle.txt points.txt")
        return

    circle_file = sys.argv[1]
    points_file = sys.argv[2]

    with open(circle_file, "r", encoding="utf-8") as f:
        line = f.readline().strip()
        cx, cy = map(float, line.split())
        r = float(f.readline().strip())

    r2 = r * r

    with open(points_file, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue  
            x, y = map(float, line.split())
            dx = x - cx
            dy = y - cy
            dist2 = dx*dx + dy*dy

            if dist2 == r2:
                print("0")  
            elif dist2 < r2:
                print("1") 
            else:
                print("2") 
main()
