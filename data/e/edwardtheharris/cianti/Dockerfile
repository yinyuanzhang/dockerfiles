FROM alpine:latest

ARG CIANTI_JOURNAL_DIR=/srv/fava
ARG CIANTI_JOURNAL_FILE=/srv/fava/cianti.bean

RUN mkdir -p $CIANTI_JOURNAL_DIR
COPY cianti.bean $CIANTI_JOURNAL_FILE

RUN apk add --no-cache alpine-sdk bash git libxml2-dev libxslt-dev python3 python3-dev py3-pip vim
RUN git clone https://github.com/edwardtheharris/beancount /srv/beancount
RUN pip3 install --upgrade pip
RUN pip3 install -e /srv/beancount
RUN pip3 install --no-cache-dir fava fava-plugins
RUN mkdir -p /srv/fava
EXPOSE 5000

CMD /usr/bin/fava -d --host 0.0.0.0 $CIANTI_JOURNAL_FILE
