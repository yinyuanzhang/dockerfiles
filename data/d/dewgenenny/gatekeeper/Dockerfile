FROM python:3

ADD gatekeeper.py /
ADD trigger.sh /

RUN pip install "websocket-client==0.54.0"
RUN pip install slackclient
RUN pip install prometheus_client

CMD [ "python", "./gatekeeper.py" ]
