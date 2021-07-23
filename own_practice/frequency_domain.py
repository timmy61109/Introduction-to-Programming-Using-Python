"""FFT."""
import matplotlib.pyplot as plt
import numpy as np


SAMPLING_RATE = 44100  # 設定取樣率 8000Hz
FFT_SIZE = 512  # 設定FFT大小

time_smpline = np.arange(0, 1.0, 1.0 / SAMPLING_RATE)

frequency = np.sin(2 * np.pi * 861.328125 * time_smpline) + \
    np.sin(2 * np.pi * 8613.28125 * time_smpline)

xs = frequency[:FFT_SIZE]
xf = np.fft.rfft(xs) / FFT_SIZE

freqs = np.linspace(0, int(SAMPLING_RATE / 2), int(FFT_SIZE / 2 + 1))
xfp = 20 * np.log10(np.clip(np.abs(xf), 1e-20, 1e100))

plt.plot(xfp, 'b')
plt.xlabel("Frequency", fontsize=14)  # x label
plt.ylabel('time(s)', fontsize=14)
plt.title('FFT')
plt.savefig('./fft.png')
plt.show()
