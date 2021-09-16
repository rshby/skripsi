from pymongo.common import RETRY_READS
from Models.heart import Database as DatabaseHeart
from Models.databaru import Database as DatabaseBaru
import json

db_heart = DatabaseHeart()
db_baru = DatabaseBaru()

# function yang digunakan untuk merubah ObjectID ke String
def ObjToStr(obj):
    try:
        return str(obj["_id"]["$oid"])
    except Exception as e:
        print(f"kesalahan function ObjToStr: {e}")

# function yang digunakan untuk melihat semua data
def viewAllDataHeart():
    try:
        dbhasil = db_heart.showAllDataHeart()
        hasil = json.loads(dbhasil)
        data_list = []
        for data in hasil:
            data["id"] = ObjToStr(data)
            data_list.append(data)
        return data_list
    except Exception as e:
        print(f"kesalahan function viewAllDataHeart: {e}")

# function yang digunakan untuk melihat semua databaru
def viewAllDataBaru():
    try:
        dbhasil = db_baru.showAllDatabaru()
        hasil = json.loads(dbhasil)
        data_list = []
        for data in hasil:
            data["id"] = ObjToStr(data)
            data_list.append(data)
        return data_list
    except Exception as e:
        print(f"kesalahan function viewAllDataBaru: {e}")

# function yang digunakan untuk insert ke databaru
def tambahDataBaru(**params):
    try:
        db_baru.insertDatabaru(**params)
        data = {
            "msg" : "ok"
        }
        return data
    except Exception as e:
        print(f"kesalahan function tambahDataBaru: {e}")