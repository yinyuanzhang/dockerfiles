FROM python:3.7-alpine
COPY dist /root/dist

RUN pip install hbmqtt && \
    mv /root/dist/* /etc/

EXPOSE 1883

CMD hbmqtt -c /etc/hbmqtt.conf
