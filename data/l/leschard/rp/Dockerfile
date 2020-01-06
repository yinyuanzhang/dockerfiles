FROM nginx:1.17

RUN apt-get update \
  && apt-get install -y --no-install-recommends --no-install-suggests curl \
  && rm -rf /var/lib/apt/lists/*

VOLUME /etc/letsencrypt/
VOLUME /etc/nginx/

EXPOSE 80
EXPOSE 443

STOPSIGNAL SIGTERM

CMD ["nginx", "-g", "daemon off;"]
