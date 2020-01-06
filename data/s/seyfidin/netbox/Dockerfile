FROM ubuntu:latest

RUN apt update
RUN apt-get install -y python3 python3-pip python3-dev build-essential libxml2-dev libxslt1-dev libffi-dev graphviz libpq-dev libssl-dev redis-server zlib1g-dev git supervisor nginx
RUN mkdir -p /opt/netbox/ && cd /opt/netbox/ && git clone -b master https://github.com/netbox-community/netbox.git . && pip3 install -r requirements.txt && pip3 install gunicorn

COPY netbox.conf /etc/supervisor/conf.d/netbox.conf
COPY init /init

ENTRYPOINT [ "/init" ]
