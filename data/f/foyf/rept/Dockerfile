FROM python:alpine

WORKDIR /myapp
COPY ./* /myapp/

RUN apk update
RUN apk add mariadb-dev gcc mariadb-connector-c-dev musl-dev
RUN pip install serial
RUN pip install sqlalchemy
RUN pip install mysqlclient

CMD [ "python","/myapp/listener.py" ]