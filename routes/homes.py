from fastapi import APIRouter        #서브용 from import 
from fastapi.templating import Jinja2Templates
router = APIRouter()

from starlette.responses import HTMLResponse
from fastapi import Request
#html 툴이 있는 폴더 위치
templates = Jinja2Templates(directory = "templates/")

# /home
# @router.get("/", response_class = HTMLResponse)                                                       
# async def home():                                                   
#     # return {"message": "home"}
#     html = "<body><h2> It is home. </h2></body>"
#     return html

@router.get("/")
async def home(request : Request) :
    pass
    return templates.TemplateResponse(name="homes/standard.html", context={"request" : request})

# /home/list
@router.get("/list", response_class = HTMLResponse) # 어노테이션 : 웹에서 업무(function)을 호출하는 기능
async def home_list() :
    # return 0
    html = "<body><h2> It is home list. </h2></body>"
    return html