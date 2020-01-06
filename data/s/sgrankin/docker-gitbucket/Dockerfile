FROM sgrankin/docker-openjdk32

RUN apk add --no-cache runit

ARG VERSION=4.11
ADD https://github.com/gitbucket/gitbucket/releases/download/$VERSION/gitbucket.war /gitbucket.war

COPY entrypoint.sh /entrypoint.sh

VOLUME /data
EXPOSE 8080

CMD ["/entrypoint.sh"]
