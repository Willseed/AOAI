from PIL import Image
from io import BytesIO
import json
import requests
from openai import AzureOpenAI

def download_images(client: AzureOpenAI, prompts: list[str]):
    for index, prompt in enumerate(prompts):
        result = client.images.generate(
            model="Dalle3",
            prompt=prompt,
            n=1
        )

        image_url = json.loads(result.model_dump_json())['data'][0]['url']

        response = requests.get(image_url)

        # 確認請求成功
        if response.status_code == 200:
            # 將內容讀取為二進制流
            image_data = BytesIO(response.content)
            
            # 使用Pillow開啟圖片
            img = Image.open(image_data)
            
            # 儲存圖片到本地
            img.save(f"downloaded_image{index}.jpg")
            print("圖片已成功下載並儲存")
        else:
            print("無法下載圖片，HTTP狀態碼：", response.status_code)