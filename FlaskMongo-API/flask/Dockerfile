FROM python:3.10.6
ADD mongo.py .
WORKDIR /mongo
COPY ./requirements.txt /mongo/requirements.txt   
RUN pip install -r requirements.txt
COPY . /mongo
EXPOSE 5000
CMD [ "python" , "./mongo.py" , "--host=0.0.0.0"]