FROM i386/debian:jessie-slim

COPY ./enum4linux /usr/bin/enum4linux
COPY ./enum4linux.pl /usr/share/enum4linux/enum4linux.pl
RUN apt-get update && apt-get install -y smbclient && mkdir -p /usr/share/enum4linux

CMD /bin/sh
