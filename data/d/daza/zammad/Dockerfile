FROM ubuntu:16.04

RUN apt-get update && apt-get upgrade -y && apt-get install wget make g++ gcc ruby-dev rubygems libmysqlclient-dev git -y

RUN echo "net.ipv6.conf.all.disable_ipv6 = 1\nnet.ipv6.conf.default.disable_ipv6 = 1\nnet.ipv6.conf.lo.disable_ipv6 = 1" >> /etc/sysctl.conf && cat /etc/sysctl.conf && sysctl -p

RUN useradd zammad -m -d /opt/zammad -s /bin/bash && cd /opt && wget https://ftp.zammad.com/zammad-latest.tar.gz && tar -xzf zammad-latest.tar.gz -C zammad && rm zammad-latest.tar.gz

COPY bundle5.sh /
RUN su - zammad && cd /opt/zammad && gem update --system && gem update && gem install bundler && bash /bundle5.sh && bundle update && gem update && gem install json -v 1.8.6 && gem uninstall json -v 2.1.0 

COPY database.yml /opt/zammad/config
COPY start.sh /root/

RUN export RAILS_ENV=production && chmod +x /root/start.sh && mkdir -p /var/log/zammad/

EXPOSE 80 

RUN apt-get install nginx -y

COPY nginx.conf /etc/nginx/

CMD ["/root/start.sh"]