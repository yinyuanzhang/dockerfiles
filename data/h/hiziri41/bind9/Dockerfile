FROM debian

RUN apt update
RUN apt upgrade -y
RUN apt install -y bind9

# ADD bind /etc/bind
# RUN chmod 640 /etc/bind/*.conf && chown bind /etc/bind/*.conf

EXPOSE 53/udp 53

ENTRYPOINT service bind9 start && tail -f /dev/null
