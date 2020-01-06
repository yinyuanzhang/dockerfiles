ARG BASEIMAGE=alpine:3.7
FROM ${BASEIMAGE}

ARG BUILD_DATE
ARG VCS_REF
ARG VERSION
LABEL mantainer="Eloy Lopez <elswork@gmail.com>" \
    org.label-schema.build-date=$BUILD_DATE \
    org.label-schema.name="Samba" \
    org.label-schema.description="Multiarch Samba for amd64 arm32v7 or arm64" \
    org.label-schema.url="https://deft.work" \
    org.label-schema.vcs-ref=$VCS_REF \
    org.label-schema.vcs-url="https://github.com/DeftWork/samba" \
    org.label-schema.vendor="Deft Work" \
    org.label-schema.version=$VERSION \
    org.label-schema.schema-version="1.0"

RUN apk update && apk upgrade && apk add bash samba-common-tools samba && rm -rf /var/cache/apk/*

COPY entrypoint.sh /entrypoint.sh
RUN chmod u+x /entrypoint.sh

EXPOSE 445 137 138 139

ENTRYPOINT ["/entrypoint.sh"]
CMD ["-h"]
