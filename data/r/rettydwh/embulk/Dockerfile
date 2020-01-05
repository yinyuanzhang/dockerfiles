FROM java:8
MAINTAINER makoto-nagai

ENV EMBULK_VERSION=0.8.38 \
    PATH_TO_EMBULK=/opt/embulk \
    PATH=${PATH}:/opt/embulk
RUN mkdir -p ${PATH_TO_EMBULK} \
    && curl -L "https://bintray.com/artifact/download/embulk/maven/embulk-${EMBULK_VERSION}.jar" -o "${PATH_TO_EMBULK}/embulk" \
    && chmod +x "${PATH_TO_EMBULK}/embulk"

WORKDIR "${PATH_TO_EMBULK}"
COPY \
    Gemfile \
    script/substitute_credential \
    script/docker_entrypoint.sh \
    "${PATH_TO_EMBULK}/"
RUN ${PATH_TO_EMBULK}/embulk bundle install

ENTRYPOINT ["bash", "./docker_entrypoint.sh"]
CMD ["--help"]
