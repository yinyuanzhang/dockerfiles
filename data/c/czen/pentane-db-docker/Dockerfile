FROM ubuntu:16.04

RUN apt-get update && \
    apt-get install -y curl && \
    apt-get install -y python3 python3-pip && \
	apt-get install -y libmysqlclient-dev && \
    pip3 install flask flask_sqlalchemy flask_marshmallow flask_migrate marshmallow-sqlalchemy requests mysqlclient flask_wtf wtforms
    