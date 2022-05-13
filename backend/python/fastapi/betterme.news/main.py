import uvicorn
from threading import Thread

def run_web():
  print("run web")
  #uvicorn.run("app.app:app",host="0.0.0.0",port=8080)
  uvicorn.run("app.main:app",port=8081)

def web_alive():
  t = Thread(target=run_web)
  t.start()

web_alive()
