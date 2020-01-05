FROM jess/telize:latest

RUN apk update && apk add supervisor && rm -rf /var/cache/apk/*

COPY supervisord.conf /etc/supervisord.conf

RUN apk update && apk add supervisor curl && rm -rf /var/cache/apk/*

COPY update-geodb.sh /etc/periodic/weekly/update-geodb.sh
COPY telize.conf /etc/nginx/conf.d/telize.conf

EXPOSE 80

CMD ["supervisord"]
