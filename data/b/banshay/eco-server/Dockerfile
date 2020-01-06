FROM mono:5.14.0

ADD startup /sbin/startup

RUN apt update \
    && chmod 755 /sbin/startup

WORKDIR /ext/eco/
EXPOSE 3000-3001

ENTRYPOINT ["/bin/sh", "--"]
CMD ["/sbin/startup"]
