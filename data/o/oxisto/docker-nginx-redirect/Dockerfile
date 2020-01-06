FROM nginx:alpine

WORKDIR /

ADD docker-entrypoint.sh .
ADD default.conf.template /etc/nginx/conf.d

CMD ["/docker-entrypoint.sh"]
