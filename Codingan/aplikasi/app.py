from fastapi import FastAPI, Request
from Controllers import heart

app = FastAPI()

# route API untuk melihat semua data
@app.get("/heart/all")
def lihatSemuaDataHeart():
    try:
        hasil = heart.viewAllDataHeart()
        return hasil
    except Exception as e:
        print(f"kesalahan function lihatSemuaData: {e}")