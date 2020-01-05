# vim:set ft=dockerfile:
FROM alpine:3.9

RUN mkdir -p /app
WORKDIR /app

RUN wget -q http://downloadfiles.idera.com/stage/IderaSQLDiagnosticManagerForMySQL-Linux-x64-tar.zip -O - | unzip -p - | tar -xzf -

ADD ./MONyog.ini ./MONyog/

VOLUME [ "/app/MONyog/data" ]

EXPOSE 5555

CMD ./MONyog/bin/MONyog-bin
