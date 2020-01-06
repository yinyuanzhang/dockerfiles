FROM alpine:3.5

RUN apk --update add --no-cache openssh bash \
    && rm -rf /var/cache/apk/* \
    && mkdir -p /root/.ssh \
    && chmod 700 /root/.ssh
    
COPY ssh_config sshd_config /etc/ssh/
COPY start.sh /
EXPOSE 22
ENTRYPOINT ["/start.sh"]