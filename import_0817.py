#要先pip install mysql-connector-python
import mysql.connector

# 連接到MySQL數據庫
mydb = mysql.connector.connect(
    host="localhost",     # XAMPP默認的MySQL主機
    user="root",          # MySQL用户名，默認为root
    password="00000000",          # MySQL密碼，默認為空
    database="database" # 要連接的數據庫名稱
)

# 如果連接成功，輸出成功信息
if mydb.is_connected():
    print("Connected to MySQL database!")

# 關閉數據庫連接
mydb.close()

