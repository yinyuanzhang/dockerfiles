###############################################################
# Copyright (C) 2019 Duall Sistemas Ltda.
###############################################################

###############################################################
# Preparing the environment:
#
# docker build --force-rm -t firebird .
# docker run -p 3050:3050 -v <your-dir>:/var/lib/firebird/3.0/data -dt --restart always firebird
###############################################################

FROM debian:buster-slim

LABEL Maintainer="Duall Sistemas <duallsistemas@gmail.com>"
LABEL Name="Firebird"
LABEL Version="3.0"

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update && apt-get install -qy --no-install-recommends \
    firebird3.0-server && \
    apt-get autoremove && apt-get autoclean && rm -rf /var/lib/apt/lists/*

RUN \
    ln -s /usr/bin/isql-fb /usr/bin/isql && \
    sed -i 's/ISC_PASSWORD=.*/ISC_PASSWORD=masterkey/' \
        /etc/firebird/3.0/SYSDBA.password && \
    sed -i 's/RemoteBindAddress = localhost/RemoteBindAddress = /g' \
        /etc/firebird/3.0/firebird.conf && \
    echo "ALTER USER sysdba SET password 'masterkey';" | isql \
        -u sysdba -p masterkey /var/lib/firebird/3.0/system/security3.fdb && \
    echo 'duall = /var/lib/firebird/3.0/data/duall.fdb' >> \
        /etc/firebird/3.0/databases.conf && \
    chown firebird:firebird -R /var/lib/firebird/3.0/data/*

VOLUME [ "/var/lib/firebird/3.0/data" ]

EXPOSE 3050/tcp

CMD [ "fbguard" ]
