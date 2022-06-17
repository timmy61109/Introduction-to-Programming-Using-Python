"""Plotting using PolyCollection in matplotlib.

PolyCollection expects a sequence of vertices, which matches your desired data
pretty well.
"""

from matplotlib.collections import PolyCollection
import matplotlib.pyplot as plt
import numpy as np
import pymysql

# 載入訓練資料
cnx = pymysql.connect(
    user='ele',
    passwd='openele',
    host='127.0.0.1',
    db='pm',
    port=3306,
    charset='utf8'
)
cursor = cnx.cursor()

# 執行 MySQL 查詢指令
cursor.execute("SELECT * FROM pm_data")

# 取回所有查詢結果
results = cursor.fetchall()

pm_data = []
COUNT = 0
count_data = []
for record in results:
    COUNT += 1
    pm_data.append([record[2], record[3], record[3]])
    count_data.append([COUNT])

pm_data_array = np.array(pm_data)
count_array = np.array(count_data)

# These will be (200, 4), (200, 4), and (4)
freq_data = count_array.astype('float32') * np.ones(3)[None, :]
amp_data = pm_data_array.astype('float32')
rad_data = np.linspace(0, 2, 3)

verts = []
for irad in range(len(rad_data)):
    # I'm adding a zero amplitude at the beginning and the end to get a nice
    # flat bottom on the polygons
    xs = np.concatenate(
        [[freq_data[0, irad]], freq_data[:, irad], [freq_data[-1, irad]]])
    ys = np.concatenate([[0], amp_data[:, irad], [0]])
    verts.append(list(zip(xs, ys)))

poly = PolyCollection(verts, facecolors=['g', 'c', 'y'])
poly.set_alpha(0.7)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# The zdir keyword makes it plot the "z" vertex dimension (radius)
# along the y axis. The zs keyword sets each polygon at the
# correct radius value.
ax.add_collection3d(poly, zs=rad_data, zdir='y')

ax.set_xlim3d(freq_data.min(), freq_data.max())
ax.set_xlabel('Time')
ax.set_ylim3d(rad_data.min(), rad_data.max())
ax.set_ylabel('Three kinds of PM \n(green pm1, blue pm2.5, yellow pm10)')
ax.set_zlim3d(amp_data.min(), amp_data.max())
ax.set_zlabel('PM')

plt.savefig('./3D.png')
plt.show()
