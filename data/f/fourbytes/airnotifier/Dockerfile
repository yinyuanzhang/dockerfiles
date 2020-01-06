FROM python:2.7

ENV DEBIAN_FRONTEND=noninteractive TERM=linux

EXPOSE 80
VOLUME ["/config", "/var/airnotifier", "/var/log/airnotifier"]

RUN apt-get update && \
    apt-get install -y --no-install-recommends ca-certificates && \
    mkdir -p /var/airnotifier/pemdir

WORKDIR /airnotifier

ADD ["requirements.txt", "."]
RUN pip install --upgrade -r requirements.txt

ADD [".", "."]

ENTRYPOINT ["/bin/bash", "start.sh"]
