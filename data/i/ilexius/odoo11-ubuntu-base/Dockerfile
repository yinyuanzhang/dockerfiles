FROM ubuntu:16.04
MAINTAINER ilexius GmbH <info@ilexius.de> 

# Setup python and java and base system 
ENV DEBIAN_FRONTEND noninteractive 
ENV LANG=C.UTF-8


#build-essential libldap2-dev libsasl2-dev

RUN apt-get update && \
  apt-get upgrade -y && \
  apt-get install -q -y --no-install-recommends \
			git \
			adduser ssh postgresql-client\
        python3 \
        python3-babel \
        python3-dateutil \
        python3-decorator \
        python3-docutils \
        python3-feedparser \
        python3-gevent \
        python3-html2text \
        python3-pil \
        python3-jinja2 \
        python3-lxml \
        python3-mako \
        python3-mock \
        python3-ofxparse \
        python3-passlib \
        python3-psutil \
        python3-psycopg2 \
        python3-pydot \
        python3-pyparsing \
        python3-pypdf2 \
        python3-reportlab \
        python3-requests \
        python3-serial \
        python3-suds \
        python3-tz \
        python3-usb \
        python3-vatnumber \
        python3-werkzeug \
        python3-xlsxwriter \
		python3-yaml \
            ca-certificates \
            curl \
            node-less \
            python3-pip \
            python3-setuptools \
            python3-renderpm \
            libssl-dev \
            xz-utils \
        && curl -o wkhtmltox.tar.xz -SL https://github.com/wkhtmltopdf/wkhtmltopdf/releases/download/0.12.4/wkhtmltox-0.12.4_linux-generic-amd64.tar.xz \
        && echo '3f923f425d345940089e44c1466f6408b9619562 wkhtmltox.tar.xz' | sha1sum -c - \
        && tar xvf wkhtmltox.tar.xz \
        && cp wkhtmltox/lib/* /usr/local/lib/ \
        && cp wkhtmltox/bin/* /usr/local/bin/ \
		&& cp -r wkhtmltox/share/man/man1 /usr/local/share/man/
		
COPY requirements.txt /root/
		
RUN pip3 install --upgrade pip requests
RUN pip3 install -r /root/requirements.txt

#missing
#python3-vobject