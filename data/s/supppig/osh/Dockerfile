FROM debian:latest
LABEL maintainer="https://github.com/supppig"

RUN mkdir -m 777 /vvv
ADD v /vvv/v
RUN chmod 777 /vvv/v 

ADD entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh 

EXPOSE 8080
ENTRYPOINT bash /entrypoint.sh
