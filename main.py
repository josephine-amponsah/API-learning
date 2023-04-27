from fastapi import FastAPI, Query
from pydantic import BaseModel
from typing import Annotated, Union


app = FastAPI()


class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None


@app.get("/items/")
async def create_item(item: Item):
    return item

# limiting length of optional query parameter


@app.get("/item/")
async def read_items(q: Annotated[Union[str, None], Query(max_length=50)] = None):
    # sourcery skip: simplify-dictionary-update
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results
