###PYTHON
FROM python:3.9

###COPY
COPY ./betterme /app/betterme
COPY ./requirements.txt /app

###WORKDIR
WORKDIR /app

###RUN INSTALL COMMANDS
RUN pip install -r requirements.txt
RUN pip install pymongo[srv]
RUN pip install jinja2

###ADD DIRECTORIES

# in file 
ADD betterme/model.py                                     app/betterme
ADD betterme/load_page_engine.py                          app/betterme
ADD betterme/easy_json/easy_json.py                       app/betterme

# in deeper file
ADD betterme/database/mongodb/discord_user_database.py    app/betterme
ADD betterme/database/mongodb/rac_database.py             app/betterme

ADD betterme/bettermenews_database/add_new_data.py        app/betterme

# directory in :app
ADD betterme/static                                       app/betterme


#PORT
EXPOSE 8080

#CMD
CMD ["uvicorn", "betterme.main:app", "--host=0.0.0.0", "--reload"]