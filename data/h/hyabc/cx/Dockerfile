FROM ubuntu:16.04
RUN apt update
RUN apt install -y supervisor python-pip unzip
RUN pip install obfsproxy
ADD gost /usr/bin/gost
ADD v2ray.zip /v2ray.zip
RUN chmod +x /usr/bin/gost
RUN unzip /v2ray.zip
RUN chmod +x /v2ray
ADD zzsupervisord.conf /etc/supervisord.conf
EXPOSE 1067
CMD ["/usr/bin/supervisord"]
