from fastapi import FastAPI

app = FastAPI()
#app = FastAPI()이므로 이후 FastAPI안에 있는 function을 사용할때 app을 사용하여 뒤에 function을 입력하여 사용
from fastapi.middleware.cors import CORSMiddleware
# No 'Access-Control-Allow-Origin'
# CORS 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 실제 운영 환경에서는 접근 가능한 도메인만 허용하는 것이 좋습니다.
    allow_credentials = True,
    allow_methods=["*"],
    allow_headers=["*"],
)
from routes.homes import router as event_router     #routes의 home 파일로부터 router를 가져올건데 event_router이라 칭할 것임.
app.include_router(event_router, prefix="/home") # 루트라고 생각하고 생각하면됨.

from fastapi import Request
from fastapi.templating import Jinja2Templates

#html 툴이 있는 폴더 위치
templates = Jinja2Templates(directory = "templates/")

@app.get("/")                                                       # input받는 업무          
async def root(request : Request):                                                   # input받는 해당값
    return templates.TemplateResponse("index.html",{"request" : request})

# study_pythons - demo server
# #while True : 
#     work, value = input("업무 / 해당값 : ").split()
#     print("work : {}, value : {}".format(work,value))