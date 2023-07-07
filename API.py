import service
from service import gen_text

from fastapi import FastAPI
app = FastAPI()
@app.get("/chat")
#@app.post("/chat")

def hello(question = None):
    #question = input("ask a question: ")
    if question is None:
        text = "ask me a question!"
        #time.sleep(5)
    else:
        text = gen_text(question)
        text = text[0]['generated_text']
    return text 