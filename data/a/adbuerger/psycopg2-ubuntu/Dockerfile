FROM adbuerger/supervisor-ubuntu

MAINTAINER Adrian Buerger <adrian.buerger@hs-karlsruhe.de>

RUN apt-get update
RUN apt-get -y install python-pip libpq-dev python-dev && \
    pip install psycopg2 && \
    apt-get -y remove python-pip python-dev && \
    apt-get -y autoremove

