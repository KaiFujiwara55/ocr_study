from fastapi import FastAPI, UploadFile, File
from PIL import Image
from io import BytesIO
import pyocr

app = FastAPI()


@app.post("/upload/")
async def upload_image(file: UploadFile = File(...)):
    # アップロードされた画像をバイナリ形式で読み込む
    contents = await file.read()
    # バイナリデータをImageクラスのインスタンスに変換する
    img = Image.open(BytesIO(contents))
    
    # tesseractを受け取る
    pyocr.tesseract.TESSERACT_CMD = '/usr/local/bin/tesseract'
    tools = pyocr.get_available_tools()
    tool = tools[0]
    builder = pyocr.builders.TextBuilder()

    result = tool.image_to_string(img, lang="jpn_vert", builder=builder)
    data_list = [text for text in result.split('\n') if text.strip()]
    data = "".join(data_list)
    
    # ここで画像処理や他の操作を行うことができます
    return {"ocr_result": data}
