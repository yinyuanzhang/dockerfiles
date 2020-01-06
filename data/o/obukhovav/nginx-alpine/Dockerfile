FROM alpine:latest
LABEL maintainer="ObukhovAV"
#Установка баш
RUN apk add --update bash && rm -rf /var/cache/apk/*
#Установка даты и времени
RUN apk add -U tzdata
RUN cp /usr/share/zoneinfo/Europe/Moscow /etc/localtime
#дополнение для проверки папок bash в запуске шелл скрипта
RUN apk add coreutils
#Nginx и прочее
RUN apk update && apk add nginx
RUN mkdir -p /run/nginx
RUN apk add nano && apk add mc && apk add curl

COPY default1.conf /etc/nginx/conf.d
RUN rm /etc/nginx/conf.d/default.conf
RUN echo "ng-tst-new" > /var/www/localhost/index.html
CMD ["nginx", "-g", "daemon off;"]
