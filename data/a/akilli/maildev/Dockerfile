FROM akilli/node

LABEL maintainer="Ayhan Akilli"

RUN npm install -g \
        maildev && \
    rm -rf \
        /root/.config \
        /root/.npm

COPY s6/ /s6/maildev/
