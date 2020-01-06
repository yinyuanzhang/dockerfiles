FROM ubuntu:16.04
RUN apt update
RUN apt install -y supervisor python-pip
RUN pip install obfsproxy
ADD gost /usr/bin/gost
RUN chmod +x /usr/bin/gost
ADD config.json /config.json
ADD exciting /exciting
RUN chmod +x /exciting
ADD zzsupervisord.conf /etc/supervisord.conf
EXPOSE 8438
CMD ["/usr/bin/supervisord"]
