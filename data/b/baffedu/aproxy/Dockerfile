FROM nginx:1.16-alpine

ADD conf.d/ /etc/nginx/conf.d/

ADD ./run.sh /
RUN chmod 777 /run.sh

# 环境变量
ENV TYPE="laravel"
ENV FPM_HOST="fpm-host"

VOLUME /var/www/html
WORKDIR /var/www/html
# RUN sh /run.sh
ENTRYPOINT [ "sh","/run.sh" ]
EXPOSE 80