FROM java:8-jdk-alpine

RUN apk add --no-cache curl libc6-compat \
    && curl --create-dirs -o /usr/local/share/embulk/bin/embulk -L "https://dl.embulk.org/embulk-latest.jar" \
    && chmod +x /usr/local/share/embulk/bin/embulk \
    && apk del --purge curl

RUN mkdir -p /usr/local/share/embulk/gem
ENV GEM_HOME /usr/local/share/embulk/gem

WORKDIR /usr/local/share/embulk

ENTRYPOINT ["java", "-jar", "/usr/local/share/embulk/bin/embulk"]

CMD ["--help"]
