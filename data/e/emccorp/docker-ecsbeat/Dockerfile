FROM frolvlad/alpine-glibc
MAINTAINER lida.he@dell.com

RUN apk add --no-cache \
      ca-certificates \
      curl

WORKDIR /ecsbeat

ADD ecsbeat-linux-amd64 /ecsbeat/ecsbeat
ADD ecsbeat.yml /ecsbeat/
ADD ecsbeat.template* /ecsbeat/
ADD entrypoint.sh /ecsbeat/entrypoint.sh

ENTRYPOINT ["/ecsbeat/entrypoint.sh"]
CMD ["/ecsbeat/ecsbeat", "-e", "-v", "-c", "/ecsbeat/ecsbeat-out.yml"]
