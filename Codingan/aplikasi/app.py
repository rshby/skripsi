from fastapi import FastAPI, Request
from Controllers import heart
import uvicorn
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:8000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# route API untuk melihat semua data
@app.get("/heart/all")
def lihatSemuaDataHeart():
    try:
        hasil = heart.viewAllDataHeart()
        return hasil
    except Exception as e:
        print(f"kesalahan function lihatSemuaData: {e}")

# route API untuk melihat prediksi data
@app.get("/predict")
def prediksiData(age: int, sex: int, cp: int, trestbps: int, chol: int, fbs: int, restecg: int, thalach: int, exang: int, oldpeak: float, slope: int, ca: int, thal: int):
    try:
        params = {
            "age": age,
            "sex": sex,
            "cp": cp,
            "trestbps": trestbps,
            "chol": chol,
            "fbs": fbs,
            "restecg": restecg,
            "thalach": thalach,
            "exang": exang,
            "oldpeak": oldpeak,
            "slope": slope,
            "ca": ca,
            "thal": thal
            }
        return heart.prediksiData(**params)
    except Exception as e:
        print(f"kesalahan function prediksiData: {e}")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8005)