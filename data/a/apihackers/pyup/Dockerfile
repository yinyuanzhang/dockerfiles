FROM alpine:3.7

ARG VCS_REF
ARG BUILD_DATE
ARG VERSION

LABEL org.label-schema.vcs-ref=$VCS_REF \
      org.label-schema.vcs-url="https://github.com/apihackers/docker-pyup" \
      org.label-schema.build-date=$BUILD_DATE \
      org.label-schema.version=$VERSION \
      org.label-schema.schema-version="1.0"

COPY requirements.pip /tmp/requirements.pip

RUN apk add --no-cache python3 ca-certificates && \
    python3 -m ensurepip && \
    rm -r /usr/lib/python*/ensurepip && \
    pip3 install --upgrade pip setuptools && \
    pip3 install -r /tmp/requirements.pip && \
    rm -r /root/.cache

ENTRYPOINT ["/usr/bin/pyup"]
