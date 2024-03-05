from typing import Union

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from backend.data_getter import MandelbrotSetGetter

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")




@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/mandlebrot_set")
def get_mandlebrot_set_data():
    data_getter = MandelbrotSetGetter()
    width = 1000
    height = 1000
    max_iter = 100
    return {
        "data": data_getter.get_mandelbrot_set(-2, 1, -1.5, 1.5, width, height, max_iter).tolist(),
        "width": width,
        "height": height,
        "max_iter": max_iter

    }