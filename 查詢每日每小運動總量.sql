SELECT member_id,運動開始時間,(運動結束時間 - 運動開始時間) AS 運動時間,運動成績 AS 每日每小時運動成績
FROM 會員運動紀錄
GROUP BY 運動開始時間;
