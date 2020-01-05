FROM ubuntu:16.04
RUN apt update
RUN apt install -y supervisor python-pip
RUN pip install obfsproxy
ADD gost /usr/bin/gost
RUN chmod +x /usr/bin/gost
ADD zzsupervisord.conf /etc/supervisord.conf
EXPOSE 1067
CMD ["/usr/bin/supervisord"]
