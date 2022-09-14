FROM python:3.10.6
WORKDIR /mongo
ADD . /mongo
RUN pip install --upgrade pip   
RUN pip install -r requirements.txt
CMD ["uwsgi","app.ini"]
