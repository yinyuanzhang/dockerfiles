FROM alpine:latest

ENV VERSION=0.9.2
ENV GLIDER_ONLY=true

WORKDIR /srv/

ADD scripts /srv/

RUN apk add --no-cache tzdata tar wget && \
    mkdir /srv/glider && \
    wget "https://github.com/nadoo/glider/releases/download/v${VERSION}/glider_${VERSION}_linux_amd64.tar.gz" -O /srv/glider/glider-linux-amd64.tar.gz && \
    cd /srv/glider && \
    tar -zxvf /srv/glider/glider-linux-amd64.tar.gz "glider_${VERSION}_linux_amd64/glider" --strip-components=1 && \
    chmod +x /srv/*.sh && \
    chmod +x /srv/glider/glider && \
    apk del tar wget && \
    rm -rf /srv/glider/glider-linux-amd64.tar.gz

VOLUME [ "/srv/glider/config" ]

CMD ["/srv/glider/glider","-config","/srv/glider/config/glider.conf"]
