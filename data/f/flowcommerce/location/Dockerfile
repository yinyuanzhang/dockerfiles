FROM flowdocker/play_builder:0.1.10 as builder
ADD . /opt/play
WORKDIR /opt/play
RUN SBT_OPTS="-Xms1024M -Xmx2048M -Xss2M -XX:MaxMetaspaceSize=2048M" sbt clean stage

FROM flowdocker/play:0.1.10
COPY --from=builder /opt/play /opt/play
WORKDIR /opt/play/api/target/universal/stage
ENTRYPOINT ["java", "-jar", "/root/environment-provider.jar", "--service", "play", "location", "bin/location-api"]
HEALTHCHECK --interval=5s --timeout=5s --retries=10 \
  CMD curl -f http://localhost:9000/_internal_/healthcheck || exit 1
