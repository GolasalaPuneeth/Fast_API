from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import uvicorn
from Open_AI_Decorator import intell
from pydantic import BaseModel

class LoginRequest(BaseModel):
    InputMessage: str
    

users = []

app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/chatter")
async def read_item(request: Request):
    return templates.TemplateResponse("index.html",{"request": request, "users":users})

@app.post("/chatter_response")
async def chat_tester(request :Request, InputMessage :str = Form(...)):
    print(InputMessage)
    Answer = intell(InputMessage)
    quireee = {
    "question": f"{InputMessage}",
    "answer": f"{Answer}"
    }
    users.append(quireee)
    return templates.TemplateResponse("index.html",{"request": request, "users":users})




if __name__ == '__main__':
    uvicorn.run(app, host="192.168.1.18", port=8000)