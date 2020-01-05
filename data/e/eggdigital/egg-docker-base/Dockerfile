FROM composer/satis:latest

WORKDIR /satis

# Install Nginx

RUN apk update \
    && apk add nginx

COPY nginx.conf /etc/nginx/nginx.conf
COPY nginx.vh.default.conf /etc/nginx/conf.d/default.conf

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]

# Set up cron
ADD crontab /var/spool/cron/crontabs/root
RUN apk add dcron wget rsync ca-certificates tzdata && rm -rf /var/cache/apk/* \
    && chmod 0600 /var/spool/cron/crontabs/root

# Set Timezone
RUN cp /usr/share/zoneinfo/Asia/Bangkok /etc/localtime \
  && apk del tzdata

# Add Satis Config

COPY pull /usr/local/bin

COPY satis.json /root

RUN sed -i -r 's/192.168.120.71:8888/35.224.111.214/g' /root/satis.json
