FROM alpine:latest

ENV PUID 0
ENV PGID 100
ENV PERMISSION 0777

# Install packages
RUN apk update
RUN apk add --no-cache \
  tzdata \
  transmission-daemon \
  openjdk8 \
  nginx \
  jq
RUN apk search -qe 'php7*' | xargs apk add

# Set locale and timezone
ENV TZ Asia/Seoul
ENV LANG ko_KR.UTF-8
ENV LANGUAGE ko_KR.UTF-8
ENV LC_ALL ko_KR.UTF-8
RUN cp /usr/share/zoneinfo/Asia/Seoul /etc/localtime
RUN echo Asia/Seoul > /etc/timezone

# Set config files
RUN mkdir -p /run/nginx /defaults
COPY ./defaults/settings.json /defaults/settings.json
COPY ./defaults/default.conf /etc/nginx/conf.d/default.conf
RUN chown root:root /etc/nginx/conf.d/default.conf
RUN chmod 775 /etc/nginx/conf.d/default.conf

# Ports and volumes
EXPOSE 80 4040 8080 9091 51413 51413/udp
VOLUME /transmission /showdown /output /showdown-manager

# Set initial script
COPY ./defaults/init.sh /init
RUN chown root:root /init
RUN chmod 555 /init

# Define entrypoint
ENTRYPOINT /init
