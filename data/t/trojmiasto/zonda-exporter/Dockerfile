FROM alpine:3.7

LABEL maintainer "Jakub Roczniewski <j.roczniewski@trojmiasto.pl>"

RUN apk update \
		&& apk add py-pip bash py-mysqldb \
		&& pip install flask pyyaml requests flask-restful gunicorn

RUN mkdir /exporter

WORKDIR /exporter

COPY run.sh /exporter
COPY zonda-exporter.py /exporter

RUN chmod +x /exporter/run.sh

EXPOSE 5002

ENTRYPOINT ["./run.sh"]
