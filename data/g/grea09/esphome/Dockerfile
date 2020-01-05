FROM python:alpine

WORKDIR /config

RUN pip install -U https://github.com/platformio/platformio-core/archive/develop.zip
RUN pip install esphome

EXPOSE 6052/tcp

ENTRYPOINT ["esphome"]
CMD ["/config", "dashboard"]
