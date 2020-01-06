FROM alpine:latest

RUN apk add postgresql-dev gcc python3-dev musl-dev

RUN pip3 install --upgrade pip
RUN pip3 install psycopg2
RUN pip3 install configparser
RUN apk add build-base
RUN apk update
RUN apk upgrade

COPY config.py /config.py
COPY config.pyc /config.pyc
COPY transaction.py /transaction.py
COPY entrypoint.sh /entrypoint.sh

RUN mkdir conf
RUN chmod +x /conf/
COPY BancoWeb.ini /conf/BancoWeb.ini
RUN chmod +x /conf/BancoWeb.ini
 
RUN chmod +x /config.py
RUN chmod +x /config.pyc
RUN chmod +x /transaction.py
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]


