FROM python:3.6-slim
ENV PYTHONUNBUFFERED 1
RUN mkdir /furniture_api
WORKDIR /furniture_api
COPY requirements.txt /furniture_api/
RUN pip install -r requirements.txt
COPY . /furniture_api/
