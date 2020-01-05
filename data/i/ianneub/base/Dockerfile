FROM ubuntu:14.04

ADD build.sh /
RUN /build.sh && rm /build.sh

ADD supervisord.conf /etc/supervisor/supervisord.conf

CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/supervisord.conf"]
