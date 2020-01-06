FROM ubuntu:18.04

# Update ubuntu
RUN apt-get update
RUN apt-get dist-upgrade -y

# get needed packages
RUN apt-get install -y nginx wget python3-minimal python3-pip

COPY default /etc/nginx/sites-available/default

ADD requirements.txt /requirements.txt
RUN pip3 install -r requirements.txt

COPY python_mirror.py /usr/local/src/python_mirror.py

ADD start.sh /start.sh

RUN chmod 700 /start.sh

EXPOSE 80

CMD ["./start.sh"]