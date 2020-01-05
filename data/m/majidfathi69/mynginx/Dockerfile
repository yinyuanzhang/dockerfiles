FROM debian:jessie

RUN apt-get update \
  &&   apt-get install nginx -y

EXPOSE 80 443

CMD ["nginx", "-g", "daemon off;"]
