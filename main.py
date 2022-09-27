from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Mahasiswa(BaseModel):
    name: str
    nim: str

dataMahasiswa = {
    "nama": "Muhammad Rey Shazni Helmi",
    "nim": "18220013"
}

@app.get("/")
def root():
    return {"data": "18220013_Tugas FastAPI"}

@app.get("/get-data/")
def get_data():
    return dataMahasiswa

@app.post("/input-data/")
def input(mahasiswa: Mahasiswa):
    dataMahasiswa = {"nama": mahasiswa.name, "nim": mahasiswa.nim}
    return dataMahasiswa