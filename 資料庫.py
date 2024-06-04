import mysql.connector

# 建立資料庫連接
mydb = mysql.connector.connect(
  host="localhost",
  user="root",  # 資料庫用戶名
  password="",  # 資料庫密碼
  database="mysql"  # 資料庫名稱
)

# 創建游標對象
mycursor = mydb.cursor()

# 從鏡頭檢測中獲取使用者的辨識碼和跳繩次數
user_id = 495049  # 假設使用者的辨識碼，再另外改成跳繩系統的參數
jump_count = 100  # 假設使用者跳繩的次數，同上

# 插入數據的 SQL 語句
sql = "INSERT INTO jump_records (id, times) VALUES (%s, %s)"
val = (user_id, jump_count)  # 將使用者的辨識碼和跳繩次數作為元組傳遞給 SQL 語句

# 執行 SQL 語句
mycursor.execute(sql, val)

# 確認數據庫操作
mydb.commit()

print(mycursor.rowcount, "record inserted.")
