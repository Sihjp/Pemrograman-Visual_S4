import matplotlib.pyplot as plt
import numpy as np

x1 = 100
y1 = 200
x2 = 100
y2 = 1000

lw = int(10)
hw = int(lw/2)

row = 1080
col = 1920

Gambar = np.zeros(shape=(row, col, 3), dtype=np.int16)

# Menggambar titik pertama
for i in range(x1-hw, x1+hw):
    for j in range(y1-hw, y1+hw):
        if 0 <= j < row and 0 <= i < col:  # Memeriksa batas indeks
            Gambar[j, i, 0] = 255

# Menggambar titik kedua
for i in range(x2-hw, x2+hw):
    for j in range(y2-hw, y2+hw):
        if 0 <= j < row and 0 <= i < col:  # Memeriksa batas indeks
            Gambar[j, i, 0] = 255

# Handle special case when y2 == y1 to avoid division by zero
if y2 != y1:
    # Calculate the slope of the line
    m = (x2 - x1) / (y2 - y1)
else:
    m = 0  # Set slope to 0 for horizontal line

# Calculate the y-intercept
c = y1 - m * x1

# Draw the line using the equation y = mx + c
for y in range(min(y1, y2), max(y1, y2) + 1):
    x = int((y - c) / m) if m != 0 else x1  # Use the equation for x if slope is not 0
    for i in range(-hw, hw + 1):
        for j in range(-hw, hw + 1):
            if 0 <= y + j < row and 0 <= x + i < col:  # Memeriksa batas indeks
                Gambar[y + j, x + i] = [6, 255, 64]  # Set all color channels to green

# Plotting the image
plt.figure()
plt.imshow(Gambar)
plt.show()