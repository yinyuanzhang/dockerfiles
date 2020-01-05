FROM node:10.16-alpine
WORKDIR /app/
RUN echo "http://dl-cdn.alpinelinux.org/alpine/edge/main" > /etc/apk/repositories && \
    echo "http://dl-cdn.alpinelinux.org/alpine/edge/community" >> /etc/apk/repositories && \
    echo "http://dl-cdn.alpinelinux.org/alpine/edge/testing" >> /etc/apk/repositories && \
    apk update && \
    apk upgrade --update-cache --available && \
    apk add icu-libs ttf-dejavu firefox && \
    wget https://github.com/mozilla/geckodriver/releases/download/v0.24.0/geckodriver-v0.24.0-linux64.tar.gz && \
    tar -xzf geckodriver-v0.24.0-linux64.tar.gz -C /usr/local/bin && \
    rm -rf /var/cache/apk/* geckodriver-v0.24.0-linux64.tar.gz
COPY package.json yarn.lock ./
RUN ["yarn", "install"]
COPY app.js ./
CMD ["node", "app.js"]
