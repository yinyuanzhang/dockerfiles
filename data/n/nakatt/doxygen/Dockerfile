FROM openjdk:8-jre-alpine
LABEL maintainer="nakat-t <armaiti.wizard@gmail.com>" \
      description="Docker image for Doxygen documentation generator."

RUN echo http://dl-cdn.alpinelinux.org/alpine/edge/main/ >> /etc/apk/repositories
RUN echo http://dl-cdn.alpinelinux.org/alpine/edge/testing/ >> /etc/apk/repositories

ENV DOXYGEN_VERSION=1.8.16-r1
ENV GRAPHVIZ_VERSION=2.40.1-r1
ENV PLANTUML_VERSION=1.2019.12
ENV PLANTUML_INSTALL_DIR=/opt/plantuml

RUN apk add --no-cache doxygen=${DOXYGEN_VERSION} graphviz=${GRAPHVIZ_VERSION} fontconfig ttf-dejavu font-ipa curl \
	&& mkdir -p ${PLANTUML_INSTALL_DIR} \
	&& curl -L https://sourceforge.net/projects/plantuml/files/plantuml.${PLANTUML_VERSION}.jar/download -o ${PLANTUML_INSTALL_DIR}/plantuml.jar \
	&& apk del curl

WORKDIR /data
ENTRYPOINT ["doxygen"]
