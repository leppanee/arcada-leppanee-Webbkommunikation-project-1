from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()

origins = ['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return { "msg": "Hello! Leppanee Repo", "v": "0.1" }


@app.get("/items/{id}")
def read_item(item_id: int, q: str = None):
    return {"id": id, "q": q}

@app.get("/api/ip")
def returnIP(request: Request):
    ip = request.client.host
    return {"ip": ip}

hotelRooms = [
{"roomNumber": 1,
 "size": 1,
 "beds": 2},
{"roomNumber": 2,
 "size": 3,
 "beds": 16},
{"roomNumber": 3,
 "size": 1,
 "beds": 2},
{"roomNumber": 4,
 "size": 2,
 "beds": 4}
]

@app.get("/rooms/")
def get_rooms():
    return hotelRooms