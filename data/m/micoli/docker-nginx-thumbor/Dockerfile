FROM nginx:1.11.5
MAINTAINER Edu Herraiz <ghark@gmail.com>

COPY etc/  /etc/
COPY ./docker-entrypoint.sh /

ENTRYPOINT ["/docker-entrypoint.sh"]
CMD ["nginx-daemon"]
