from typing import TypedDict


class Car(TypedDict, total=False):
    transmission: str
    year: int
    price: int
    fuel: str
    paint_color: str
    drive: str
    type: str
    make: str
    manufacturer: str
    miles: int
    title_status: str
