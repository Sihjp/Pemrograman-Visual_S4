
import matplotlib.pyplot as plt
import numpy as np

# The user informs the coordinates of the four points for the lines.
# a points = (100, 200)
x1 = 100
y1 = 200
# b points = (800, 600)
x2 = 800
y2 = 600
# c points = (1800, 200)
x3 = 1800
y3 = 200
# d points = (100, 1000)
x4 = 100
y4 = 1000

# The user declares the line width
lw = int(10)

# Calculate the half line width
hw = int(lw / 2)

# Setting the size of the canvas
row = int(1080)
col = int(1920)
print('col, row =', col, ',', row)

# Preparing the black canvas
gambar = np.zeros(shape=(row, col, 3), dtype=np.uint16)

# Function to draw a line between two points
def draw_line(x1, y1, x2, y2):
    if x2 == x1:
        # Handle vertical lines
        x = x1
        y_start = min(y1, y2)
        y_end = max(y1, y2)
        for y in range(y_start, y_end + 1):
            for i in range(-hw, hw + 1):
                for j in range(-hw, hw + 1):
                    if 0 <= y + j < row and 0 <= x + i < col:
                        gambar[y + j, x + i] = [6, 255, 64]
    else:
        # Calculate the slope (m) and y-intercept (c)
        m = (y2 - y1) / (x2 - x1)
        c = y1 - m * x1

        # Determine the start and end points for drawing the line
        x_start = min(x1, x2)
        x_end = max(x1, x2)

        # Draw the line
        for x in range(x_start, x_end + 1):
            y = int(m * x + c)
            for i in range(-hw, hw + 1):
                for j in range(-hw, hw + 1):
                    if 0 <= y + j < row and 0 <= x + i < col:
                        gambar[y + j, x + i] = [6, 255, 64]

# Draw lines between a-b, b-c, c-d
draw_line(x1, y1, x2, y2)
draw_line(x1, y1, x3, y3)
draw_line(x1, y1, x4, y4)


for i in range(x1 - hw, x1 + hw):
    for j in range(y1 - hw, y1 + hw):
        if ((i - x1) * 2 + (j - y1) * 2) < hw ** 2:
            gambar[j, i, 0] = 255

for i in range(x2 - hw, x2 + hw):
    for j in range(y2 - hw, y2 + hw):
        if ((i - x2) * 2 + (j - y2) * 2) < hw ** 2:
            gambar[j, i, 0] = 255

for i in range(x3 - hw, x3 + hw):
    for j in range(y3 - hw, y3 + hw):
        if ((i - x3) * 2 + (j - y3) * 2) < hw ** 2:
            gambar[j, i, 0] = 255

for i in range(x4 - hw, x4 + hw):
    for j in range(y4 - hw, y4 + hw):
        if ((i - x4) * 2 + (j - y4) * 2) < hw ** 2:
            gambar[j, i, 0] = 255

plt.figure()
plt.imshow(gambar)
plt.show()