FROM python:3.7-alpine

ENV PORT 5443
EXPOSE ${PORT}/tcp

ENV TARGET http://localhost/write?db=iot

RUN mkdir -p /home/ssl

ADD laso_influxdb_decoder_proxy.py /home/
ADD laso_influxdb_decoder_proxy /home/
ADD test_* /home/
ADD Pipfile /home/

RUN pip install pipenv && cd /home && pipenv install -d && pipenv run pytest && pipenv uninstall --all-dev && rm test_*

WORKDIR /home
ENTRYPOINT pipenv run python ./laso_influxdb_decoder_proxy.py

