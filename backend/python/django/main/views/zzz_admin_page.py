from .zzz_oauth import (
    # function
    is_admin
)
from .auto_scrap import *
from .forms import MultiForm

#lib
import os
import json,io
from dotenv import load_dotenv


load_dotenv()
OAUTH_URL = os.getenv("OAUTH_URL")

#django
from django.http import HttpResponse
from django.template.response import TemplateResponse

async def auto_scrap( request,  page_number: int):

  ad_check = is_admin(request.COOKIES.get("discord_access_token"))
  print('call auto scrap')
  if ad_check == True:

      #return scrap_by_page_number(page_number)
      scraping = scrap_by_page_number(page_number)
      return TemplateResponse(request,"auto-scrap.html",{
        "scraping": scraping,
        "topics": topic
        })

  else:
    content =  f"""
    <html>
      <a href={OAUTH_URL}>dang nhap</a>
    </html>
    """

    response = HttpResponse(content)
    response.set_cookie(key="pre_page",value=f"auto-scrap/{page_number}")

    return response

async def scrap_check(request,name: str,
  #html_type: str = Form(...),
  #tags: list = Form(...)
  ):

  with open('check_data.json', encoding='utf-8') as f1:
    all_post = json.load(f1)

  name = "/"+name
  url = "https://khoahoc.tv" + name
  thumbnail_link = all_post[name]['thumb_src']
  name = title_process(name)
  

  data = await test_create_data(url,name,"normal",thumbnail_link,"","",['khoa-hoc'])
  #print(data)

  description = data["description"]
  keywords = data["keywords"]
  html_type = data["html_type"]
  content = data["content"]

  
  return TemplateResponse(request, "demo_news_post.html",
    {
    "description": description,
    "keywords": keywords,
    "html_type": html_type,
    "content": content
    })

async def scrap_confirm(request):

  if request.method == "POST":

    check_list = request.POST.getlist('check_list')
    html_type = request.POST.getlist('html_type')
    tags = request.POST.getlist('tags')

    if 'add-one' in request.POST:
      if request.POST['add-one'] in check_list:
        print(check_list)
        print(html_type)
        print(tags)

        await auto_scrap_process(check_list,html_type,tags)

    elif 'add-all' in request.POST:
      
      check_list = request.POST.getlist('check_list')
      print(check_list)
      print(html_type)
      print(tags)

      await auto_scrap_process(check_list,html_type,tags)

    return HttpResponse("done")

def hello(request):
  return HttpResponse('hello world')