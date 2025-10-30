import numpy as np
import cv2
from my_module.K21999.lecture05_camera_image_capture import MyVideoCapture

def lecture05_01():

    # カメラキャプチャ実行
    app = MyVideoCapture()
    app.run()
    app.write_img()

    def get_img(self) -> np.ndarray | None:
        """最後にキャプチャされた画像を取得する。

        Returns:
            np.ndarray | None: キャプチャされた画像（BGR形式）。未取得の場合は None。
        """
        return self.captured_img


    # 画像をローカル変数に保存
    google_img : cv2.Mat = cv2.imread('images/google.png')
    capture_img : cv2.Mat = cv2.imread('output_images/camera_capture.png') # 動作テスト用なので提出時にこの行を消すこと
    # capture_img : cv2.Mat = "implement me"

    g_hight, g_width, g_channel = google_img.shape
    c_hight, c_width, c_channel = capture_img.shape
    print(google_img.shape)
    print(capture_img.shape)

    for x in range(g_width):
        for y in range(g_hight):
            g, b, r = google_img[y, x]
            # もし白色(255,255,255)だったら置き換える
            if (b, g, r) == (255, 255, 255):
                google_img[y, x] = capture_img[y, x]
                #google画像と

                #implement me

    # 書き込み処理
    cv2.imwrite('images/google_with_capture.png', google_img)
    # implement me

