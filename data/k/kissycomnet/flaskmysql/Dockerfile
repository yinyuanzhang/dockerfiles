

FROM python:3.6-slim

#ENV db_username
#ENv db_password
#ENV db_name
#ENV ipaddress


RUN apt-get clean \
    && apt-get -y update

RUN apt-get -y install \
    nginx \
    python3-dev \
    build-essential

WORKDIR /app

COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt --src /usr/local/src

COPY app.py /app/app.py
COPY db_config.py /app/db_config.py
COPY startup.sh /app/startup.sh
COPY uwsgi.ini /app/uwsgi.ini

COPY nginx.conf /etc/nginx

RUN chmod +x ./startup.sh

EXPOSE 8080

CMD [ "./startup.sh" ]

