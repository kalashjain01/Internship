FROM python:3.10.3
ADD app.py .
WORKDIR /
COPY ./requirements.txt /requirements.txt   
RUN pip install -r requirements.txt
COPY . /
EXPOSE 5000
CMD [ "python" , "./app.py" , "--host=0.0.0.0"]