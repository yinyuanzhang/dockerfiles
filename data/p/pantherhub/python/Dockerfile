FROM pantherhub/python:2.7
MAINTAINER Panther Hub

WORKDIR /usr/src/app

ONBUILD COPY . .
ONBUILD COPY requirements.txt ./
ONBUILD RUN pip install --no-cache-dir -r requirements.txt

CMD [ "python","./start.py" ]