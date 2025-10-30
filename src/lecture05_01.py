import cv2
import numpy as np
from my_module.K21999.lecture05_camera_image_capture import MyVideoCapture

def lecture05_01():
    # 1. カメラキャプチャ
    cam = MyVideoCapture()
    cam.run()
    capture_img = cam.get_img()

    if capture_img is None:
        print("カメラキャプチャが取得できませんでした。")
        return

    # 2. Google画像を読み込む
    google_img = cv2.imread('images/google.png')
    if google_img is None:
        print("images/google.png が見つかりません。")
        return

    g_h, g_w, _ = google_img.shape
    c_h, c_w, _ = capture_img.shape

    # 3. 白部分をカメラ画像で置換
    for y in range(g_h):
        for x in range(g_w):
            b, g, r = google_img[y, x]
            if (b, g, r) == (255, 255, 255):
                y_c = y % c_h
                x_c = x % c_w
                google_img[y, x] = capture_img[y_c, x_c]

    # 4. 保存
    output_path = 'output_images/lecture05_01_k24086.png'
    cv2.imwrite(output_path, google_img)
    print(f"保存しました: {output_path}")
