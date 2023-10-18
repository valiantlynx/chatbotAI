from typing import Union, Optional
from fastapi import FastAPI, Request, Header
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from src.train import train
from src.chat import chat

app = FastAPI()
origins = [
    "https://valiantlynx.github.io/htmx-chat/",
    "https://valiantlynx.github.io",
    "http://localhost",
    "http://localhost:8000",
    "http://127.0.0.1:5500",
    "http://127.0.0.1"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/src/static", StaticFiles(directory="src/static"), name="static")

templates = Jinja2Templates(directory="src/templates")
 
import debugpy
debugpy.listen(("0.0.0.0", 5678))

# the AI chatbot code starts here
train()

# Serve index.html on the root path ("/")
@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# Notice that you have to pass the request as part of the key-value pairs in the context for Jinja2. So, you also have to declare it in your path operation.
@app.get("/chat", response_class=HTMLResponse)
async def read_item(request: Request, q: Union[str, None] = None, hx_request: Optional[str] = Header(None)):
    print("received: ", q)
    res = chat(q)
    print("res: ", res)
    context = {"request": request, "q": q, "res": res}
    if hx_request:
        return templates.TemplateResponse("bubble.html", context)
    
    return  {"question": q, "response": res}

