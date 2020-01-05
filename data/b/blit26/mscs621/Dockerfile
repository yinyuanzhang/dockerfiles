FROM ubuntu:18.04

MAINTAINER Brandon Litwin "brandon.litwin1@marist.edu"

RUN apt-get update -y && \
    apt-get install -y python-pip python-dev

ENV FLASK_APP="app/app.py"

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

COPY . /app

EXPOSE 5000

CMD ["flask", "run", "--host", "0.0.0.0"]

RUN python app/load_db.py