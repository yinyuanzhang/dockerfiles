FROM gradle:5.6.2-jdk11

USER root
WORKDIR /
RUN mkdir -p /in && mkdir -p /src/main/proto
VOLUME /in
COPY *.gradle /
RUN gradle --no-daemon clean -PprotobufVersion=3.9.1 -PgrpcVersion=1.23.0
ENTRYPOINT ["gradle", "--no-daemon", "publish"]
