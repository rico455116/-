SELECT member_id,SUM(運動成績) AS 總成績
FROM 會員運動紀錄
GROUP BY member_id
ORDER BY 總成績 DESC;
