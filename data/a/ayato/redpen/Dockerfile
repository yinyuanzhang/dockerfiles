FROM java:openjdk-8-alpine

WORKDIR /tmp

RUN apk add --update --no-cache --virtual redpen-deps openssl
RUN wget -q https://github.com/redpen-cc/redpen/releases/download/redpen-1.9.0/redpen-1.9.0.tar.gz -O - | tar xz && \
    cp -av redpen-distribution-1.9.0/* /usr/local/ && \
    rm -rf redpen-distribution-1.9.0/
RUN apk del --purge redpen-deps

RUN export PATH=$PATH:/usr/local/bin

CMD ["redpen"]