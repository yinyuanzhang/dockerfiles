ARG JAVA_MAJOR_VERSION="13"
ARG JAVA_MINOR_REVISION="0.1"
ARG JAVA_BUILD_NUMBER="9"
ARG JAVA_BUILD_PATH="cec27d702aa74d5a8630c65ae61e4305"
ARG JAVA_VERSION=${JAVA_MAJOR_VERSION}.${JAVA_MINOR_REVISION}
ARG JAVA_HOME_DIR=java-${JAVA_VERSION}_${JAVA_BUILD_NUMBER}-openjdk-amd64
ARG JAVA_HOME=/usr/lib/jvm/${JAVA_HOME_DIR}
ARG JAVA_SHA256="2e01716546395694d3fad54c9b36d1cd46c5894c06f72d156772efbcf4b41335"

FROM buildpack-deps:curl AS downloader

ARG JAVA_MAJOR_VERSION
ARG JAVA_MINOR_REVISION
ARG JAVA_BUILD_NUMBER
ARG JAVA_BUILD_PATH
ARG JAVA_VERSION
ARG JAVA_HOME_DIR
ARG JAVA_HOME
ARG JAVA_SHA256

RUN apt-get update && apt-get install -y --no-install-recommends \
		bzip2 \
		unzip \
		xz-utils \
		ca-certificates \
	&& apt-get autoremove --purge -y \
	&& apt-get clean \
	&& rm -rf /var/lib/apt/lists/*

ENV JAVA_HOME ${JAVA_HOME}
ARG JAVA_URL="https://download.java.net/java/GA/jdk${JAVA_VERSION}/${JAVA_BUILD_PATH}/${JAVA_BUILD_NUMBER}/GPL/openjdk-${JAVA_VERSION}_linux-x64_bin.tar.gz"

ARG basedir=${JAVA_HOME}
ARG mandir=$basedir/man

RUN mkdir -p /usr/lib/jvm/ \
 && TMP_DIR=$(mktemp -d) \
 && cd ${TMP_DIR} \
 && wget ${JAVA_URL} \
 && echo "${JAVA_SHA256} openjdk-${JAVA_VERSION}_linux-x64_bin.tar.gz" | sha256sum -c - \
 && tar xf openjdk-${JAVA_VERSION}_linux-x64_bin.tar.gz -C /usr/lib/jvm/ \
 && cd /usr/lib/jvm/ \
 && mv jdk-${JAVA_VERSION} ${JAVA_HOME_DIR}

FROM python:slim

LABEL maintenar="Kenji Saito <ken-yo@mbr.nifty.com>"

RUN apt-get update \
 && apt-get full-upgrade -qqy \
 && apt-get install -y --no-install-recommends \
		xz-utils \
		ca-certificates \
 && apt-get autoremove --purge -y \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

# Default to UTF-8 file.encoding
ENV LANG C.UTF-8

ARG JAVA_MAJOR_VERSION
ARG JAVA_BUILD_NUMBER
ARG JAVA_VERSION
ARG JAVA_HOME_DIR
ARG JAVA_HOME

ENV JAVA_HOME ${JAVA_HOME}

ARG basedir=${JAVA_HOME}
ARG mandir=${basedir}/man

COPY --from=downloader ${JAVA_HOME} ${JAVA_HOME}

RUN set -ex; \
	\
# deal with slim variants not having man page directories (which causes "update-alternatives" to fail)
	if [ ! -d /usr/share/man/man1 ]; then \
		mkdir -p /usr/share/man/man1; \
	fi; \
	\
    mkdir -p /usr/lib/jvm/; \
    ln -s ${JAVA_HOME_DIR} java-${JAVA_MAJOR_VERSION}-openjdk-amd64 \
    ; \
    for i in $(ls ${basedir}/bin); do \
        update-alternatives --install /usr/bin/${i} ${i} $basedir/bin/${i} 1100; \
    done \
 && \
# update-alternatives so that future installs of other OpenJDK versions don't change /usr/bin/java
    update-alternatives --get-selections | awk -v home="$(readlink -f "$JAVA_HOME")" 'index($3, home) == 1 { $2 = "manual"; print | "update-alternatives --set-selections" }'; \
# ... and verify that it actually worked for one of the alternatives we care about
	update-alternatives --query java | grep -q 'Status: manual'

ENV PATH ${JAVA_HOME}/bin:${PATH}

HEALTHCHECK CMD [ "java", "-version" ]

RUN groupadd -g 1000 java \
 && useradd -g 1000 -l -m -s /bin/false -u 1000 java

USER java

CMD ["jshell"]
