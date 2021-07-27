"""Spectrogram."""
from matplotlib.colors import BoundaryNorm
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
import numpy as np
from scipy.io import wavfile


# 讀入單一檔案測試
sampling_rate, frequency = wavfile.read('c9DxQmY.wav')
sampling_rate = 512
print(sampling_rate)

for size in range(len(frequency) // sampling_rate):
    xs = frequency[size * sampling_rate:(size + 1) * sampling_rate] / 2 ** 24.0
    xf = np.fft.rfft(xs) / sampling_rate
    xfp = 20 * np.log10(np.clip(np.abs(xf), 1e-20, 1e100))
    if size == 0:
        z = np.array(xfp).reshape(len(xfp), 1)
    z = np.append(z, np.array(xfp).reshape(len(xfp), 1), axis=1)

# make these smaller to increase the resolution
dx, dy = 1, 1

# generate 2 2d grids for the x & y bounds
y, x = np.mgrid[slice(0, len(z), dy),
                slice(0, (len(frequency) // sampling_rate) + 1, dx)]

# x and y are bounds, so z should be the value *inside* those bounds.
# Therefore, remove the last value from the z array.
z = z[:-1, :-1]
levels = MaxNLocator(nbins=15).tick_values(z.min(), z.max())

# pick the desired colormap, sensible levels, and define a normalization
# instance which takes data values and translates those into levels.
cmap = plt.get_cmap('PiYG')
norm = BoundaryNorm(levels, ncolors=cmap.N, clip=True)

fig, (ax0) = plt.subplots(nrows=1)

# contours are *point* based plots, so convert our bound into point
# centers
cf = ax0.contourf(x[:-1, :-1] + dx/2.,
                  y[:-1, :-1] + dy/2., z, levels=levels,
                  cmap=cmap)
fig.colorbar(cf, ax=ax0)
ax0.set_title('Spectrogram')
plt.xlabel('Time(s)', fontsize=14)  # x label
plt.ylabel('Frequency', fontsize=14)  # y label

# adjust spacing between subplots so `ax1` title and `ax0` tick labels
# don't overlap
fig.tight_layout()
plt.savefig('./spectrogram.png')

plt.show()
