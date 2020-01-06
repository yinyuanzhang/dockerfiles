FROM debian:jessie
RUN apt-get update
RUN apt-get -y install build-essential python-dev libmysqlclient-dev
RUN apt-get -y install python3 python-pip 
RUN pip install MySQL-python
RUN apt-get install python-mysqldb
RUN pip install --upgrade django==1.3
RUN apt-get install -y git
RUN git clone https://github.com/kuthubshavali/Djangowebapp
EXPOSE 8080

