FROM pipill/armhf-alpine:3.4

MAINTAINER nimmis <kjell.havneskold@gmail.com>

COPY rootfs/ /

RUN [ "cross-build-start" ]

RUN apk update && apk upgrade && \
    apk add ca-certificates supervisor rsyslog supervisor && \
    chmod +x /my_* && \
    mkdir /etc/my_runonce /etc/my_runalways /etc/container_environment /etc/workaround-docker-2267 /var/log/supervisor && \
    touch /var/log/startup.log && chmod 666 /var/log/startup.log && \
    rm -rf /var/cache/apk/*

RUN [ "cross-build-end" ] 

# Set environment variables.
ENV HOME /root

# Define default command.
CMD ["/my_init"]

