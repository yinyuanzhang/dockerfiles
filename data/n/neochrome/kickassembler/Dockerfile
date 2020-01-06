FROM openjdk:13-alpine
ARG VERSION=5.7
WORKDIR /opt
RUN \
	echo "Fetching version ${VERSION}"; \
	wget -O- "http://theweb.dk/KickAssembler/KickAssembler${VERSION}.zip" \
	| unzip - KickAss.jar
ENTRYPOINT ["java", "-jar", "/opt/KickAss.jar"]
