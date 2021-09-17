from fastapi import FastAPI, Request
from Controllers import heart
import uvicorn

app = FastAPI()

# route API untuk melihat semua data
@app.get("/heart/all")
def lihatSemuaDataHeart():
    try:
        hasil = heart.viewAllDataHeart()
        return hasil
    except Exception as e:
        print(f"kesalahan function lihatSemuaData: {e}")

# route API untuk melihat prediksi data
@app.post("/predict")
def prediksiData(params: dict):
    try:
        return heart.prediksiData(**params)
    except Exception as e:
        print(f"kesalahan function prediksiData: {e}")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8005)