FROM ubuntu:18.04

RUN apt-get -y update \
    && apt-get install -y --no-install-recommends --no-install-suggests postgrey=1.36-5 \
    && rm -rf /var/lib/apt/lists/* \
    && rm /etc/default/postgrey \
    && touch /etc/default/postgrey \
    && echo 'POSTGREY_OPTS="--inet=0.0.0.0:10023"' > /etc/default/postgrey

RUN ln -sf /dev/stdout /var/log/mail.log

EXPOSE 10023

CMD ["postgrey", "--inet", "0.0.0.0:10023", "--delay", "50", "--user", "postgrey", "--group", "postgrey"]