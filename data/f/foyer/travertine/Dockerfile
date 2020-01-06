ARG JRE_VERSION=jre11

FROM foyer/base:$JRE_VERSION

ARG MC_VERSION=1.14
ARG TRAVERTINE_VERSION=latest
ARG BUILD_DATE
ARG VCS_REF

LABEL org.label-schema.schema-version="1.0.0" \
      org.label-schema.name=travertine \
      org.label-schema.build-date=$BUILD_DATE \
      org.label-schema.vcs-url="https://git.foyer.cool/docker-travertine" \
      org.label-schema.vcs-ref=$VCS_REF \
      cool.foyer.minecraft.version=$MC_VERSION \
      cool.foyer.travertine.version=$TRAVERTINE_VERSION

USER root
RUN curl -Lo /usr/libexec/travertine.jar https://papermc.io/api/v1/travertine/$MC_VERSION/$TRAVERTINE_VERSION/download
ADD travertine /bin/travertine
USER minecraft

EXPOSE 25577

CMD [ "travertine" ]
