FROM ubuntu:16.04

WORKDIR /tmp/

RUN apt-get update && apt-get install curl python3-minimal python3-pip git-core -y

RUN git clone https://github.com/gdomod/pewi.git .

RUN pip3 install numpy ccxt python-telegram-bot


ADD run.sh /tmp
RUN chmod +x /tmp/run.sh
RUN mkdir /etc/pewi

ENTRYPOINT ["/tmp/run.sh"]

CMD []
