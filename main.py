from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from quote_generator import *


generator = TextGenerator()
generator.load_generator()

class Quote(BaseModel):
    start_text: str
    output: str = None

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"Quotify": "Turn your words into wisdom"}

@app.post("/generate_quote/")
async def generate(quote: Quote):
    quote.output = generator.generate_text(quote.start_text)
    return {"output" : quote.output}

@app.get("/generate/{start_text}")
def read_root(start_text: str):
    output = generator.generate_text(start_text)
    return {"output" : output}

