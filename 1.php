<?php
// 載入db.php來連結資料庫
require_once 'db.php';
?>
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
    </div>

    <script>
        // 獲取計數器元素和按鈕元素
        const counterElement = document.getElementById('counter');
        const incrementBtn = document.getElementById('incrementBtn');

        // 初始化計數器值
        let count = 0;
        counterElement.textContent = count;

        // 點擊按鈕時更新計數器
        incrementBtn.addEventListener('click', function() {
            count++;
            counterElement.textContent = count;
        });
    </script>
    <?php
    $host = 'localhost';
    $dbuser ='root';
    $dbpassword = '';
    $dbname = 'member_db';
    $link = mysqli_connect($host,$dbuser,$dbpassword,$dbname);
    if($link){
        mysqli_query($link,'SET NAMES uff8');
        // echo "正確連接資料庫";
    }
    else {
        echo "不正確連接資料庫</br>" . mysqli_connect_error();
    }
?>
</body>
</html>
