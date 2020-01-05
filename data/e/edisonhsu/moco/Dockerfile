FROM java:alpine

WORKDIR /moco

COPY moco-runner-1.0.0-standalone.jar .

VOLUME ["/moco/config"]

EXPOSE 12306

ENTRYPOINT ["/usr/bin/java"]

CMD ["-jar", "moco-runner-1.0.0-standalone.jar", "http", "-p", "12306", "-c", "config/*.json"]
