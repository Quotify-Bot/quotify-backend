from fastapi import FastAPI
from pydantic import BaseModel
from quote_generator import *

generator = TextGenerator()
generator.load_generator()

class Quote(BaseModel):
    start_text: str
    output: str = None

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/generate_quote/")
async def generate(quote: Quote):
    quote.output = generator.generate_text(quote.start_text)
    return {"output" : quote.output}


