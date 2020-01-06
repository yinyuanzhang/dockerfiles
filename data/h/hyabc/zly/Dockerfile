FROM ubuntu:16.04
RUN apt update
RUN apt install -y wget nodejs git npm supervisor gcc python-pip python-dev
RUN pip install obfsproxy
RUN git clone https://github.com/hyabc/shadowsocks-heroku.git
RUN npm install ws net fs path http minimist https-proxy-agent
ADD gost /usr/bin/gost
RUN chmod +x /usr/bin/gost
RUN mkdir -p /var/log/supervisor
ADD zzsupervisord.conf /etc/supervisord.conf
EXPOSE 4681
CMD ["/usr/bin/supervisord"]
