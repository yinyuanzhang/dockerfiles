FROM pcraster/emis_base:1.0.0

MAINTAINER Kor de Jong <k.dejong1@uu.nl>

COPY cmd.sh server.py server_flask.py uwsgi.ini /
COPY emis_domain /emis_domain
COPY test /test

CMD ["/cmd.sh"]
