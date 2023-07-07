import service
from service import gen_text

from fastapi import FastAPI
app = FastAPI()
@app.get("/chat")

def hello(question = None):
    if question is None:
        text = "ask me a question!"
    else:
        text = gen_text(question)
        text = text[0]['generated_text']
    return text 