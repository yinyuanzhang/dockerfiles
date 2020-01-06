# VERSION 0.0.1
FROM centos:7
MAINTAINER iodsp<nmred_2008@126.com>

ENV NGINX_PATH=/usr/local/adinf/nginx

#get all the dependences
RUN yum install -y git gcc make wget pcre-devel zlib-devel

RUN mkdir -p ${NGINX_PATH}

# install packages
RUN mkdir work
RUN cd work/ \
    && wget http://nginx.org/download/nginx-1.12.2.tar.gz \
	&& tar -zxf nginx-1.12.2.tar.gz \
	&& cd nginx-1.12.2/ \
	&& ./configure --prefix=${NGINX_PATH} --with-stream --with-threads \
	&& make \
	&& make install


# access ports
EXPOSE 80

# 运行时产生的数据目录
VOLUME /data
# 运行时配置文件目录
VOLUME /conf
# 运行是的日志目录
VOLUME /logs
# 工作目录
WORKDIR /data


COPY start.sh /usr/bin/
#make the start.sh executable
RUN chmod 777 /usr/bin/start.sh
ENTRYPOINT ["/usr/bin/start.sh"]
