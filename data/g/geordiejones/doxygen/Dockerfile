FROM alpine:latest
MAINTAINER joneszone1975@gmail.com

ARG plantuml_install_dir=/app

ENV PLANTUML_VERSION 1.2019.6
RUN apk add --no-cache doxygen graphviz ghostscript-fonts ttf-droid ttf-droid-nonlatin curl openjdk8 \
    && mkdir $plantuml_install_dir \
    && curl -L https://sourceforge.net/projects/plantuml/files/plantuml.${PLANTUML_VERSION}.jar/download -o /$plantuml_install_dir/plantuml.jar \
    && apk del curl

ENV PLANTUML_JAR_PATH=$plantuml_install_dir/plantuml.jar

WORKDIR /data
VOLUME ["/data"]

ENTRYPOINT ["doxygen", "./Doxyfile"]
CMD ["--help"]
