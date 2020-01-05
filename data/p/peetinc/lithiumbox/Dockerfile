FROM ubuntu:latest

COPY bootstrap.sh /
COPY init.sh /

RUN /bootstrap.sh

EXPOSE 4280 4282 4285 4287

VOLUME ["/opt/proserver/db","/var/log/proserver","/var/opt/proserver"]

CMD ["/init.sh"]
