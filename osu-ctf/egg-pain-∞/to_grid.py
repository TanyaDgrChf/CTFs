from PIL import Image, ImageDraw

objs = []
qr_code = [[0 for _ in range(25)] for _ in range(25)]
offset_x = 56
inc_x = (440 - 56) / 24
offset_y = 0
inc_y = inc_x

# Parse object coordinates from file
with open('objects.txt', 'r') as f:
    for line in f:
        line = line.strip().split(',')
        objs.append((int(line[0]), int(line[1])))

# Map object coordinates to QR code matrix
for coord in objs:
    x = int((coord[0] - offset_x) / inc_x)
    y = int((coord[1] - offset_y) / inc_y)
    if 0 <= x < 25 and 0 <= y < 25:
        qr_code[x][y] = 1

for i in qr_code:
    print(i)