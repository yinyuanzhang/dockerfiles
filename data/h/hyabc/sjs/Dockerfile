FROM ubuntu:16.04
RUN apt update
RUN apt install -y wget supervisor
RUN wget https://github.com/hyabc/lantern/raw/master/lantern_linux_amd64 -O /usr/bin/lantern
RUN chmod +x /usr/bin/lantern
ADD gost /usr/bin/gost
RUN chmod +x /usr/bin/gost
RUN mkdir -p /var/log/supervisor
ADD zzsupervisord.conf /etc/supervisord.conf
EXPOSE 4681
CMD ["/usr/bin/supervisord"]
