import matplotlib.pyplot as plt
import numpy as np

x1 = 100
y1 = 200
x2 = 1800
y2 = 200

lw = int(10)

hw = int(lw/2)

row = int(1000)
col = int(1920)
print('col, row = ', col, ",", row)

Gambar = np.zeros(shape=(row, col, 3), dtype=np.int16)

for i in range(x1-hw, x1+hw):
    for j in range(y1-hw, y1+hw):
        if ((i-x1)**2 + (j-y1)**2) < hw**2:
            Gambar[j,i,0] = 255

for i in range(x2-hw, x2+hw):
    for j in range(y2-hw, y2+hw):
        if ((i-x2)**2 + (j-y2)**2) < hw**2:
            Gambar[j,i,0] = 255

# Draw the horizontal line
for x in range(x1, x2 + 1):
    y = y1  # Atur nilai y agar garis horizontal
    for i in range(-hw, hw + 1):
        for j in range(-hw, hw + 1):
            Gambar[y + j, x + i] = [6,255,64] 

plt.figure()
plt.imshow(Gambar)
plt.show()
