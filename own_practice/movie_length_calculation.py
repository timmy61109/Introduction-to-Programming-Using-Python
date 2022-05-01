"""英呎轉換格數與時間.

英呎表示：英呎輸入長度，格數輸入0
格數表示：英呎輸入0，格數輸入數量
機器表示：英呎輸入長度，格數輸入數量
"""

import ast

print("輸入英呎或機器格數，僅以其一作為計算請將未使用的輸入0")
print("""
    英呎表示：英呎輸入長度，格數輸入0
    格數表示：英呎輸入0，格數輸入數量
    機器表示：英呎輸入長度，格數輸入數量
""")

while True:
    FOOT = ast.literal_eval(input("請輸入長度(單位：英呎)："))
    GRID = ast.literal_eval(input("請輸入格數(單位：格數)："))

    FPS = FOOT * 16 + GRID
    FOOT = FPS / 16
    SECONDS = FPS / 24

    HOURS = format(SECONDS // 3600, '.0f')
    MINUTES = format((SECONDS % 3600) // 60, '.0f')
    SECONDS = ((SECONDS % 3600) % 60) / 1

    print("共", FOOT, '英呎', FPS, '畫面')
    print('時間：', HOURS, '小時', MINUTES, '分鐘', SECONDS, '秒')

    input("\n按任意鍵繼續")
    print("")
