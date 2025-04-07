# 3D анимация для примера
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import ArtistAnimation

fig = plt.figure(figsize=(10, 6))
ax_3d = fig.add_subplot(projection='3d')

x = np.arange(-2*np.pi, 2*np.pi, 0.2)
y = np.arange(-2*np.pi, 2*np.pi, 0.2)
xgrid, ygrid = np.meshgrid(x, y)

phasa = np.arange(0, 2*np.pi, 0.1)
frames = []

for p in phasa:
    zgrid = np.sin(xgrid+p) * np.sin(ygrid) / (xgrid * ygrid)

    line = ax_3d.plot_surface(xgrid, ygrid, zgrid, color='b')
    frames.append([line])

animation = ArtistAnimation(
    fig,                # фигура, где отображается анимация
    frames,             # кадры
    interval=30,        # задержка между кадрами в мс
    blit=True,          # использовать ли двойную буферизацию
    repeat=True)        # зацикливать ли анимацию

plt.show()
