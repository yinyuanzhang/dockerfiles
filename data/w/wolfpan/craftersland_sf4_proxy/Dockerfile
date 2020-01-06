FROM debian
RUN apt-get update \
  && apt-get install -y rinetd
COPY ports /etc/rinetd.conf
CMD rinetd -f -c /etc/rinetd.conf

