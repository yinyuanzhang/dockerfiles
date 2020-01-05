FROM python:3.6-slim

EXPOSE 80

WORKDIR /code

ADD app /code

RUN pip install -r requirements.txt

ENV TZ Europe/Moscow
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone


CMD ["python", "./app.py"]