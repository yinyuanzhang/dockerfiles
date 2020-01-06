FROM python:3.7-slim

RUN apt-get update && apt-get install -y --no-install-recommends git
ADD . /code       
WORKDIR /code
RUN pip install --upgrade pip setuptools && pip install -r /code/requirements.txt && pip install -e .
