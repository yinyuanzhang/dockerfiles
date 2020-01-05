FROM node
MAINTAINER huangwc@easecloud.cn

#ENV TZ=Asia/Shanghai

RUN mkdir -p /var/app
WORKDIR /var/app
VOLUME /var/app

COPY ./build.sh /var
COPY ./startup.sh /var

RUN chmod +x /var/startup.sh && chmod +x /var/build.sh
RUN /var/build.sh

EXPOSE 3000

CMD ["/var/startup.sh"]
