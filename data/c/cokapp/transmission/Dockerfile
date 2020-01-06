FROM debian:jessie

MAINTAINER Transmission Docker Maintainers "charlie@cokapp.com"

#RUN add-apt-repository -y ppa:transmissionbt/ppa && \
    #apt-get -q update && \
    #apt-get install -qy --force-yes transmission-daemon ca-certificates wget tar curl unrar-free procps && \
    #apt-get -y autoremove && \
    #apt-get -y clean && \
    #rm -rf /var/lib/apt/lists/* && \
    #rm -rf /tmp/*

#安装
RUN apt-get update && \
	apt-get install -y transmission-daemon

#安装web-control
RUN mv /usr/share/transmission/web/index.html /usr/share/transmission/web/index.original.html
ADD ./transmission-control-full.tar.gz /usr/share/transmission/

#添加配置文件
ADD ./settings.json /var/lib/transmission-daemon/info/settings.json

#添加启动脚本
ADD ./start.sh /start.sh
RUN chmod +x /start.sh


EXPOSE 9091 51413

ENV USERNAME="admin" \
    PASSWORD="password"

VOLUME ["/downloads", "/incomplete", "/watch", "/config"]

CMD ["/start.sh"]