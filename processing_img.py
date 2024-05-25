import requests
import cv2
import numpy as np

def processing(file_path):
    # 画像を読み込む
    img = cv2.imread(file_path)

    ### ここに画像処理のコードを記述してください ###
    
    ### ここに画像処理のコードを記述してください ###

    return img

if __name__ == "__main__":
    file_path = "test_img/book_jp_1.jpg"
    img = processing(file_path)
    cv2.imwrite(f'{file_path}_after.jpg', img)
    res = requests.post('http://localhost:8000/upload/', files={'file': open(f'{file_path}_after.jpg', 'rb')})

    with open(f'{file_path}_result.txt', 'w') as f:
        f.write(res.text)
