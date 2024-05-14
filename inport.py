import pymysql
import charts
# 資料庫參數設定
db_settings = {
    "host": "172.26.80.1",
    "port": 3306,
    "user": "L2B102-049\CJCU-CC",
    "db": "Master",
    "charset": "utf8"
}


try:
    # 建立Connection物件
    conn = pymysql.connect(**db_settings)

    with conn.cursor() as cursor:
              # 新增資料SQL語法
        command = "INSERT INTO charts(member_id, 運動時間, 成績)VALUES(%s, %s, %s)"
        val = ('110b13382', '2024-05-14', '20')
        mycursor.execute(command, val)

    mydb.commit()
result = cursor.fetchall()
print(result)
