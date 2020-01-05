FROM node:11-alpine

ADD start-dzldr.sh /

RUN \
    apk update && \
    apk add --no-cache \
    bash \
    ca-certificates \
    wget \
    git \
    unzip \
    jq && \
    chmod 777 /start-dzldr.sh && \
    ln -sf /root/.config/Deezloader\ Remix/ /config && \
    ln -sf /downloads /root/Deezloader\ Music
    
EXPOSE 1730

ENTRYPOINT ["./start-dzldr.sh"]