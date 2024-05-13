import cv2
import mediapipe as mp
import pandas as pd

# 初始化Mediapipe
mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

# 初始化計數器和上一幀的腳位置
jump_count = 0
prev_foot_y = None
is_rising = False

# 創建空的 DataFrame 來儲存跳繩次數
jump_data = pd.DataFrame(columns=["Frame", "Jump Count"])

# 打開攝影機
cap = cv2.VideoCapture(0)

cv2.namedWindow("Jump Rope Counter", cv2.WINDOW_NORMAL)  # 創建一個可調整大小的視窗

with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            continue

        # 轉換為RGB格式
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # 處理幀並檢測身體姿勢
        results = pose.process(frame_rgb)

        # 繪製姿勢關節點
        if results.pose_landmarks:
            mp_drawing.draw_landmarks(frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

            # 檢查左腳和右腳的關節點是否存在
            if results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_ANKLE].visibility > 0.9 and results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_ANKLE].visibility > 0.9:
                # 計算左腳和右腳的平均垂直位置
                left_foot_y = int(results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_ANKLE].y*frame.shape[0])
                right_foot_y = int(results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_ANKLE].y*frame.shape[0])
                avg_foot_y = (left_foot_y + right_foot_y) // 2

                # 判斷身體位置是否上升
                if prev_foot_y is None:
                    prev_foot_y = avg_foot_y
                if avg_foot_y < prev_foot_y:
                    is_rising = True
                elif avg_foot_y > prev_foot_y and is_rising:
                    jump_count += 1
                    is_rising = False
                    print(f"跳繩次數：{jump_count}")
                    # 將跳繩次數記錄到 DataFrame 中
                    jump_data = jump_data.append({"Frame": cap.get(cv2.CAP_PROP_POS_FRAMES), "Jump Count": jump_count}, ignore_index=True)

                prev_foot_y = avg_foot_y

        # 在幀上繪製跳繩次數
        cv2.putText(frame, f"jump count: {jump_count}", (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        # 顯示幀
        cv2.imshow("Jump Rope Counter", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

# 將 DataFrame 寫入 Excel 文件
jump_data.to_excel("jump_data.xlsx", index=False)

# 釋出資源
cap.release()
cv2.destroyAllWindows()
