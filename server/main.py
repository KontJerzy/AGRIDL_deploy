from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import numpy as np
from io import BytesIO
from PIL import Image
import tensorflow as tf
from server.config import cfg
import os

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:3000",
    "https://firatelli.com/predict",
    "https://firatelli.com",
    "http://www.firatelli.com",
    "http://www.firatelli.com/predict",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#sample_detection = DetectionSample()
#MODEL = sample_detection.get_model()
MODEL = tf.keras.models.load_model(os.path.join(cfg.ROOT_DIR, '1'))
#CLASS_NAMES = sample_detection.get_class_names()
CLASS_NAMES = ['Tomato_Bacterial_spot', 'Tomato_Early_blight', 'Tomato_Late_blight', 
               'Tomato_Leaf_Mold', 'Tomato_Septoria_leaf_spot', 'Tomato_Spider_mites_Two_spotted_spider_mite', 
               'Tomato__Target_Spot', 'Tomato__Tomato_YellowLeaf__Curl_Virus', 'Tomato__Tomato_mosaic_virus', 
               'Tomato_healthy']

@app.get("/ping")
async def ping():
    return "hi, I am alive"

def read_image(data) -> np.ndarray:
    image = np.array(Image.open(BytesIO(data)))
    return image
    

@app.post("/predict")
async def predict(
    file: UploadFile = File(...)
):
    image = read_image(await file.read())
    image_batch = np.expand_dims(image, 0)
    predictions = MODEL.predict(image_batch)
    predicted_class = CLASS_NAMES[np.argmax(predictions[0])]
    confidence = np.max(predictions[0])

    return {
        'predicted_class' : predicted_class,
        'confidence' : float(confidence)
    }


if __name__ == "__main__":
    uvicorn.run("main:app", host='localhost', port=8000, reload=True)   