FROM ubuntu:16.04
RUN apt-get update
RUN apt-get update -y
RUN apt-get install -y curl git python libpq-dev python-dev libmysqlclient-dev

RUN apt-get update
RUN apt-get install -y wget
RUN wget https://bootstrap.pypa.io/get-pip.py && python get-pip.py

RUN curl -sL https://deb.nodesource.com/setup_4.x | bash - 

ADD . /src
WORKDIR /src

RUN apt-get update -y

RUN apt-get install libffi-dev build-essential -y

RUN apt-get install python-psycopg2 -y

RUN apt-get install libmemcached-dev -y

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["python", "run.py"]