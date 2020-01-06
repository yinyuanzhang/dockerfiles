FROM nginx:alpine
ADD VERSION .
MAINTAINER Akshay Gupta
LABEL maintainer="hy.akshay@gmail.com"

RUN apk update \
    && adduser -D -u 1000 -g 'www' www \
    && mkdir /www \
    && chown -R www:www /www

COPY ./conf/nginx.conf /etc/nginx/nginx.conf
COPY ./run_nginx.sh /run_nginx.sh
COPY ./start.sh /start.sh

RUN chmod +x /run_nginx.sh /start.sh

CMD ["sh","-c","/start.sh"]

EXPOSE 80
