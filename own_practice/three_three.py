"""
程式設計練習題 2.2-2.10 3.3 幾何:計算面積.

撰寫一程式計算以下四個城市的經緯度所包圍的面積。

Atlanta, Georgia:33.7679192, -84.5606913
Orlando, Florida:28.554998, -81.381721
Savannah, Georgia: 32.0530594, -81.1733668
Charlotte, North Carolina: 35.2033919, -81.1200262

提示:
    程式設計練習題 3.2 幾何:大圓距離
    程式設計練習題 2.14 幾何:計算三角形的面積
"""
import math


atlanta_x, atlanta_y = math.radians(33.7679192), math.radians(-84.5606913)
orlando_x, orlando_y = math.radians(28.554998), math.radians(-81.381721)
savannah_x, savannah_y = math.radians(32.0530594), math.radians(-81.1733668)
charlotte_x, charlotte_y = math.radians(35.2033919), math.radians(-81.1200262)
RADIUS = 6371.01

atlanta_orlando = RADIUS * math.acos(
    math.sin(atlanta_x) * math.sin(orlando_x)
    + math.cos(atlanta_x) * math.cos(orlando_x) * math.cos(
        atlanta_y - orlando_y))

orlando_savannah = RADIUS * math.acos(
    math.sin(orlando_x) * math.sin(savannah_x)
    + math.cos(orlando_x) * math.cos(savannah_x) * math.cos(
        orlando_y - savannah_y))

savannah_charlotte = RADIUS * math.acos(
    math.sin(savannah_x) * math.sin(charlotte_x)
    + math.cos(savannah_x) * math.cos(charlotte_x) * math.cos(
        savannah_y - charlotte_y))

atlanta_charlotte = RADIUS * math.acos(
    math.sin(atlanta_x) * math.sin(charlotte_x)
    + math.cos(atlanta_x) * math.cos(charlotte_x) * math.cos(
        atlanta_y - charlotte_y))

atlanta_savannah = RADIUS * math.acos(
    math.sin(atlanta_x) * math.sin(savannah_x)
    + math.cos(atlanta_x) * math.cos(savannah_x) * math.cos(
        atlanta_y - savannah_y))

atlanta_orlando_savannah = (
    atlanta_orlando + orlando_savannah + atlanta_savannah) / 2
atlanta_orlando_savannah_area = (
    atlanta_orlando_savannah
    * (atlanta_orlando_savannah - atlanta_orlando)
    * (atlanta_orlando_savannah - orlando_savannah)
    * (atlanta_orlando_savannah - atlanta_savannah)) ** 0.5

atlanta_charlotte_savannah = (
    atlanta_charlotte + savannah_charlotte + atlanta_savannah) / 2
atlanta_charlotte_savannah_area = (
    atlanta_charlotte_savannah
    * (atlanta_charlotte_savannah - atlanta_charlotte)
    * (atlanta_charlotte_savannah - savannah_charlotte)
    * (atlanta_charlotte_savannah - atlanta_savannah)) ** 0.5

area = atlanta_orlando_savannah_area + atlanta_charlotte_savannah_area
print("The four city area is", area)
