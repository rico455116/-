<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>網頁計數器</title>
    <style>
        #counter {
            font-size: 24px;
            font-weight: bold;
            margin-bottom: 20px;
        }

        #incrementBtn {
            padding: 10px 20px;
            font-size: 18px;
            cursor: pointer;
        }
    </style>
</head>
<body>
    <h1>網頁計數器</h1>
    <div>
        <p>點擊按鈕增加計數：</p>
        <div id="counter">0</div>
        <button id="incrementBtn">增加計數</button>
		<button id="imput_sql">匯入資料庫</button>
    </div>

    <script>
        // 獲取計數器元素和按鈕元素
        const counterElement = document.getElementById('counter');
        const incrementBtn = document.getElementById('incrementBtn');        // 初始化計數器值
        let counts = 0;
        counterElement.textContent = counts;

        // 點擊按鈕時更新計數器
        incrementBtn.addEventListener('click', function() {
            counts++;
            counterElement.textContent = counts;
        });
		imput_sql.addEventListener('click', function() {
			<?php
			echo "資料庫連接中";
			$count = $_GET["counts"];
			$mysqli = new mysqli("localhost", "root","",  "member_db");
			$sql = sprintf("INSERT INTO users VALUES(\"%s\"),$count");
			if ($mysqli->query($sql) === TRUE) {
				echo "Table 'users' created successfully";
			} else {
				echo "Error creating table: " . $mysqli->error;
			}
			mysqli_close($mysqli);
			?>
        });
    </script>

</body>
</html>
