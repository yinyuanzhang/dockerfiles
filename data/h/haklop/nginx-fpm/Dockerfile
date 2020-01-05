FROM haklop/nginx-ubuntu

RUN apt-get install -y php5-fpm php5-cli php5-curl

ADD . /root/scripts

RUN chmod +x /root/scripts/run.sh

CMD ["/root/scripts/run.sh"]
