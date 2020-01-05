FROM alpine:3.10

RUN apk add --update --no-cache bash sane-saned sane-utils sane-backend-epson sane-backend-epson2 busybox-extras && \
    echo "6566 stream tcp nowait root.root /usr/sbin/saned saned" >/etc/inetd.conf && \
    addgroup saned lp


ADD https://raw.githubusercontent.com/jpetazzo/pipework/master/pipework /pipework
ADD run.sh /run.sh

EXPOSE 6566-6570

ENV DATA_PORT_RANGE="6567-6570" ALLOW_HOSTS="192.168.1.0/24 172.17.0.1/24"

CMD /run.sh
