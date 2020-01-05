FROM bitnami/minideb
LABEL maintainer="Indexyz <docker@indexyz.me>"

COPY agent /
RUN chmod +x /agent

ENTRYPOINT ["/agent"]
