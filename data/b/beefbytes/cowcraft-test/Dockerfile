FROM beefbytes/cowcraft-base
LABEL maintainer="contact@beefbytes.com"

COPY common .

USER root
RUN chown -R 1001:1001 /home/mc \
    && chmod -R 774 /home/mc

USER 1001

RUN /home/mc/server/scripts/on-build.sh