"""Time domain."""
import matplotlib.pyplot as plt
from scipy.io import wavfile


# 讀入單一檔案測試
sampling_rate, data_array = wavfile.read('c9DxQmY.wav')  # load the data

plt.plot(data_array / 2 ** 24.0, 'b')
plt.xlabel("time(s)", fontsize=14)  # x label
plt.ylabel('Hz', fontsize=14)
plt.title('Time Domain')
plt.savefig('./time_domain.png')
plt.show()
