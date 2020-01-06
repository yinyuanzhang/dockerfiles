FROM akolosov/nginx

RUN rm -f /etc/nginx/sites-enabled/default
RUN mkdir -p /app

ADD default /etc/nginx/sites-enabled/default
ADD index.html /app/index.html

# Define mount points.
VOLUME ["/data"]

RUN chmod 0777 /data
RUN mkdir -p /data/log

ENV SHELL /bin/bash

ENTRYPOINT ["/usr/sbin/nginx"]
