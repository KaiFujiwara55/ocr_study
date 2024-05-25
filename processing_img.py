import requests
import cv2
import numpy as np

def processing(file_path):
    # 画像を読み込む
    img = cv2.imread(file_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    ### ここに画像処理のコードを記述してください ###
    # img = cv2.GaussianBlur(img, (5, 5), 0)
    for threshold in range(150, 255, 3):
        th_img = cv2.threshold(img, threshold, 255, cv2.THRESH_BINARY_INV)[1]
    img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)[1]
    ### ここに画像処理のコードを記述してください ###

    return img

if __name__ == "__main__":
    file_path = "test_img/book_jp_1.jpg"
    img = processing(file_path)
    cv2.imwrite(f'{file_path}_after.jpg', img)
    res = requests.post('http://localhost:8000/upload/', files={'file': open(f'{file_path}_after.jpg', 'rb')})

    with open(f'{file_path}_result.txt', 'w') as f:
        f.write(res.text)
