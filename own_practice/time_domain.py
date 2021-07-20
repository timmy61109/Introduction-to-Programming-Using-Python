"""Time domain."""
import matplotlib.pyplot as plt
from scipy.fftpack import fft
from scipy.io import wavfile


# 讀入單一檔案測試
_, data_array = wavfile.read('c9DxQmY.wav')  # load the data
time_domain = []

# this is 16-bit track, b is now normalized on [-1, 1)
for ele in data_array:
    time_domain.append(ele / 2 ** 16.)

# calculate fourier transform (complex numbers list)
fft_data = fft(time_domain)

# you only need half of the fft list (real signal symmetry)
ranges = len(fft_data) / 2

plt.plot(time_domain, 'b')
plt.xlabel("time(s)", fontsize=14)  # x label
plt.ylabel('Hz', fontsize=14)
plt.title('Time Domain')
plt.savefig('./time_domain.png')
plt.show()

plt.plot(abs(fft_data[:]), 'r')
plt.xlabel('Hz', fontsize=14)  # x label
plt.ylabel('Size', fontsize=14)
plt.title('FFT')
plt.savefig('./fft.png')
plt.show()
