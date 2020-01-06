FROM lachlanevenson/k8s-helm

LABEL maintainer="Gustavo Hoirisch <gustavo.hoirisch@momenton.com.au>"

ARG VCS_REF
ARG BUILD_DATE

# Metadata
LABEL org.label-schema.vcs-ref=$VCS_REF \
      org.label-schema.vcs-url="https://github.com/momenton/k8s-helm" \
      org.label-schema.build-date=$BUILD_DATE \
      org.label-schema.docker.dockerfile="/Dockerfile"

ENV HELM_HOME /helm

RUN apk add --no-cache git \
    && mkdir -p $HELM_HOME/plugins \
    && helm plugin install https://github.com/chartmuseum/helm-push

ENTRYPOINT ["helm"]
CMD ["help"]
