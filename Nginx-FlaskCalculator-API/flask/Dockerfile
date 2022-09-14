FROM python:3.10.3
WORKDIR /app
ADD . /app  
RUN pip install --upgrade pip   
RUN pip install -r requirements.txt
CMD ["uwsgi","app.ini"]