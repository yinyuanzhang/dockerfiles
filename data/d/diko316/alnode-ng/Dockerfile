FROM diko316/alnode-firefox:firefox-v1.3

COPY . $PROJECT_ROOT

EXPOSE 443

RUN apk update && \
    apk add --no-cache \
        python \
        curl \
        linux-headers \
        build-base \
        paxctl \
        libgcc \
        libstdc++ \
        gnupg && \
    npm install -g --unsafe-perm "@angular/cli" && \
    apk del linux-headers \
                build-base \
                paxctl \
                libgcc \
                libstdc++ \
                gnupg && \
    rm -rf /etc/ssl \
                /usr/share/man \
                /usr/include/* \
                /tmp/* \
                /var/cache/apk/* \
                /root/.npm \
                /root/.node-gyp \
                /root/.gnupg
