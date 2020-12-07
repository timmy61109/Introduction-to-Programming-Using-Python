"""
程式設計練習題 2.2-2.10 2.5 財務應用程式:計算小費.

請撰寫一程式，將英鎊轉成公斤。讀取小記金額(subtotal)和小費率(gratuity rate)等數值，接著計算
小費及總金額。比方說，假設使用者數入小記金額為10，小費率為15%，那麼程式就會顯示1.5的小費，及
11.5的總金額。以下為範本書出樣本:
```
Enter the subtotl and a gratuity rate:15.69, 15
The gratuity is 2.35 and the total is 18.04
```
"""
import ast


SUBTOTL, gratuity_rate = ast.literal_eval(
    input("Enter the subtotl and a gratuity rate:"))

gratuity = SUBTOTL * gratuity_rate * 0.01
total = SUBTOTL + gratuity

print("The gratuity is", gratuity, "and the total is", total)
