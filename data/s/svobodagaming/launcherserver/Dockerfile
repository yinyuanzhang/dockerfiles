FROM debian:stretch-slim

RUN set -eux; \
	apt-get update; \
	apt-get install -y --no-install-recommends \
# utilities for keeping Debian and OpenJDK CA certificates in sync
		ca-certificates p11-kit \
	; \
	rm -rf /var/lib/apt/lists/*

# Default to UTF-8 file.encoding
ENV LANG C.UTF-8

RUN set -eux; \
	dpkgArch="$(dpkg --print-architecture)"; \
	case "$dpkgArch" in \
		amd64) upstreamArch='x64' ;; \
		arm64) upstreamArch='aarch64' ;; \
		*) echo >&2 "error: unsupported architecture: $dpkgArch" ;; \
	esac; \
	\
	apt-get update; \
	apt-get install -y --no-install-recommends \
		curl \
		dirmngr \
		gnupg \
		lib32z1 \
		wget \
	; \
	rm -rf /var/lib/apt/lists/*

COPY app/ /app

WORKDIR /app
RUN set -eux; \
  curl -o ./setup.sh https://launcher.sashok724.net/download/setup.sh; \
	chmod +x setup.sh; \
	./setup.sh

ENV JAVA_HOME /app/updates/jre-8u202-linux64
ENV PATH $JAVA_HOME/bin:$PATH

CMD ["java", "-Xmx256M", "-jar", "LaunchServer.jar"]

EXPOSE 7240
VOLUME ["/app"]
