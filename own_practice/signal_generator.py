"""Signal Generator."""
import matplotlib.pyplot as plt
import numpy as np


SAMPLING_RATE = 44100  # 設定取樣率 8000Hz
FFT_SIZE = 512  # 設定FFT大小

time_smpline = np.arange(0, 1.0, 1.0 / SAMPLING_RATE)

frequency = np.sin(2 * np.pi * 86.1328125 * time_smpline) + \
    np.sin(2 * np.pi * 861.328125 * time_smpline)

plt.plot(frequency, 'b')
plt.xlabel("time(s)", fontsize=14)  # x label
plt.ylabel('Frequency', fontsize=14)
plt.title('Signal Generator')
plt.savefig('./signal_generator.png')
plt.show()
