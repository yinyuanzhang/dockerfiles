FROM python:3.5.2

MAINTAINER dafire

RUN apt-get update;\
    apt-get install -y redis-server apt-utils;\
    apt-get purge -y apt-utils;\
    apt-get clean;\
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

ADD requirements.txt /tmp/requirements.txt
RUN pip install --upgrade pip; \
    pip install -r /tmp/requirements.txt; \
    rm /tmp/requirements.txt

RUN curl -sL https://deb.nodesource.com/setup_7.x | bash;\
	    apt-get install -y nodejs;\
	    apt-get -y autoremove;\
	    npm install -g bower bower-installer \
      && rm -rf /var/lib/apt/lists/*
