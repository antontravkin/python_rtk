# пробуем перерисовывать график в интерактивном режиме
import time
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-2*np.pi, 2*np.pi, 0.1)

plt.ion()  # включаем интерактивный режим работы

for delay in np.arange(0, 4*np.pi, 0.1):
    y = np.sin(x+delay)

    plt.clf()  # очищаем plt
    plt.plot(x, y)
    plt.draw()
    # используется, чтобы дать возможность пакету matplotlib обработать свои внутренние события
    plt.gcf().canvas.flush_events()

    time.sleep(0.02)

plt.ioff()  # вЫключаем интерактивный режим работы
plt.show()
