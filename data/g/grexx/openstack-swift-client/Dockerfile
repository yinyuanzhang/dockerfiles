FROM python:slim

ADD entrypoint.sh /entrypoint.sh

RUN apt-get update  \
    && apt-get install -y gcc \
    && pip install python-swiftclient \
    && pip install python-keystoneclient \
    && chmod +x entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]