FROM alpine:latest

RUN apk add --update python py-pip
RUN pip install --upgrade pip

RUN pip install requests influxdb 

COPY *.py /

ENV INFLUXHOST localhost
ENV INFLUXPORT 8086
ENV INFLUXUSER root
ENV INFLUXPASS root
ENV INFLUXDB   neurio 

ENV NEURIO_ADDR localhost

CMD [ "python", "neurio-influx.py" ]
