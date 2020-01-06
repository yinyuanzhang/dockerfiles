FROM nginx:alpine

LABEL MAINTAINER="Weerayut Hongsa <kusumoto.com@gmail.com>"

ADD . /

WORKDIR /

ENTRYPOINT [ "sh", "docker-entrypoint.sh" ]

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]