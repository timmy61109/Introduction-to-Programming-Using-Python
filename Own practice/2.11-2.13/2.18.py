"""
程式設計練習題 2.2-2.10 2.18 顯示目前時間.

輸入與GMT的時差，顯示此特定時區之時間於螢幕:

以下是輸出樣本:
```
Enter the time zone offset to GMT:-5
The current time is 4:50:34
```
"""
import time


time_zone_offset = eval(input("Enter the time zone offset to GMT:"))
time_zone_offset_seconds = time_zone_offset * 3600
currentTime = time.time()  # Get current time

# Obtain the total seconds since midnight, Jan 1, 1970
totalSeconds = int(currentTime)
totalSeconds += time_zone_offset_seconds

# Get the current second
currentSecond = totalSeconds % 60

# Obtain the total minutes
totalMinutes = totalSeconds // 60

# Compute the current minute in the hour
currentMinute = totalMinutes % 60

# Obtain the total hours
totalHours = totalMinutes // 60

# Compute the current hour
currentHour = totalHours % 24

# Display results
print("Current time is " + str(currentHour) + ":"
      + str(currentMinute) + ":" + str(currentSecond) + " GMT")
