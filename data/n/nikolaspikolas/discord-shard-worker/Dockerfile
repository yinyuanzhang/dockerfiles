FROM openjdk:11-slim as BUILDER
WORKDIR /etc/dsw
COPY ./ ./
USER root
RUN chmod +x ./gradlew
RUN ./gradlew assemble

FROM openjdk:11-slim as RUNNER
WORKDIR /etc/dsw
COPY --from=BUILDER ./etc/dsw/build/libs ./
EXPOSE 80
ENTRYPOINT java \
	-XX:+UseG1GC \
	-XX:+UseStringDeduplication \
	-XX:MaxGCPauseMillis=50 \
	-Xss250k \
	-Xmx$HEAP_SIZE \
	-XX:MaxMetaspaceSize=100m \
	-Djavax.net.ssl.trustStorePassword=changeit \
	-jar \
	./dsw.jar