FROM alpine:latest
RUN mkdir /app; apk update && apk add --no-cache python3 && rm -rf /var/cache/apk/* && pip3 install --no-cache-dir uuid requests pyyaml flask pymongo pyjwt gunicorn && addgroup -S -g 998 fordera-auth && adduser -S -D -H -u 999 -G fordera-auth fordera-auth
WORKDIR /app
ADD src /app/
USER 999
CMD gunicorn -b 0.0.0.0:8090 -w 2 wsgi
EXPOSE 8090
