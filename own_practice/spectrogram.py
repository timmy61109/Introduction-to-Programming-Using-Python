"""Spectrogram."""
from matplotlib.colors import BoundaryNorm
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
import numpy as np
from scipy.io import wavfile


# 讀入單一檔案測試
sampling_rate, frequency = wavfile.read('一分鐘，吸睛說話術-bt-_c9DxQmY.wav')
FFT_SIZE = sampling_rate
time = len(frequency) / sampling_rate
print('錄音檔共', time, '秒', '，採樣率', sampling_rate,
      '，採樣寬度為每', FFT_SIZE, '筆資料進行傅立葉轉換')

for size in range(len(frequency) // sampling_rate):
    xs = frequency[size * sampling_rate:(size + 1) * sampling_rate] / 2 ** 24.0
    xf = np.fft.rfft(xs) / sampling_rate
    xfp = 20 * np.log10(np.clip(np.abs(xf), 1e-20, 1e100))
    if size == 0:
        z = np.array(xfp).reshape(len(xfp), 1)
    z = np.append(z, np.array(xfp).reshape(len(xfp), 1), axis=1)
    print('進度', (size / (len(frequency) // sampling_rate)) * 100, '%')
    plt.plot(xfp, 'b')
    plt.xlabel("Frequency", fontsize=14)  # x label
    plt.ylabel('dB', fontsize=14)
    plt.title('FFT')
    plt.savefig('./fft' + str(size) + '.png')
    plt.close()
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
cmap = plt.get_cmap('RdBu')
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
