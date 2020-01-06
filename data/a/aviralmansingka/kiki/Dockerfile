FROM python:2.7

WORKDIR /app

ADD . /app

RUN apt-get install -y libmysqlclient-dev
RUN pip install -r requirements.txt

EXPOSE 80

ENV NAME Kiki

CMD ["python", "app.py"]
