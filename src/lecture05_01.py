import cv2
from my_module.K24083.lecture05_camera_image_capture import MyVideoCapture


def lecture05_01():

    # カメラキャプチャ実行
    print("カメラを起動します... 'q'キーを押してキャプチャしてください")
    app = MyVideoCapture()
    app.run()

    # 画像をローカル変数に保存
    google_img = cv2.imread("images/google.png")
    capture_img = app.get_img()

    # エラーチェック
    if google_img is None:
        print("エラー: 'images/google.png' が読み込めませんでした")
        return
    if capture_img is None:
        print(
            "エラー: カメラ画像が取得できませんでした。'q'キーを押してキャプチャを完了してください"
        )
        return

    g_height, g_width, g_channel = google_img.shape
    c_height, c_width, c_channel = capture_img.shape

    for x in range(g_width):
        for y in range(g_height):
            b, g, r = google_img[y, x]
            # もし白色だったら置き換える
            if (b, g, r) == (255, 255, 255):
                cap_x = x % c_width
                cap_y = y % c_height
                google_img[y, x] = capture_img[cap_y, cap_x]

    # 書き込み処理
    cv2.imwrite("output_images/lecture05_01_k24083.png", google_img)
    print("画像を 'output_images/lecture05_01_k24083.png' に保存しました")
