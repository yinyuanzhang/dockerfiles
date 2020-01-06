FROM tiangolo/uwsgi-nginx-flask:python3.7


ENV LISTEN_PORT 5000
EXPOSE 5000

COPY ./app /app
COPY requirements.txt /app/
WORKDIR /app

RUN pip install --upgrade pip
RUN pip install -r requirements.txt


