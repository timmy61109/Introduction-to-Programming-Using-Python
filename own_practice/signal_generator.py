"""Signal Generator."""
import matplotlib.pyplot as plt
import numpy as np


SAMPLING_RATE = 44100  # 設定取樣率 8000Hz
FFT_SIZE = 512  # 設定FFT大小

time_smpline = np.arange(0, 1.0, 1.0 / SAMPLING_RATE)

frequency = np.sin(2 * np.pi * 861.328125 * time_smpline) + \
    np.sin(2 * np.pi * 8613.28125 * time_smpline)
time_domain = []
for ele in frequency:
    time_domain.append(ele)

plt.plot(time_domain, 'b')
plt.xlabel("time(s)", fontsize=14)  # x label
plt.ylabel('Hz', fontsize=14)
plt.title('Time Domain')
plt.savefig('./time_domain.png')
plt.show()
