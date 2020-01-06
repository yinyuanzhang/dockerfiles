FROM python:3.7-slim

MAINTAINER tassentanne@gmail.com

ENV MYSQL_PORT 3306
ENV CROSS_ORIGIN True
ENV DEBUG False
ENV LD_LIBRARY_PATH /usr/local/lib

WORKDIR /app

# RUN apt-get install gcc

COPY requirements.txt /app/

RUN pip3 install -r requirements.txt

COPY . /app/

EXPOSE 9050

RUN python installer.py

CMD cd ./app && python app.py
