FROM beefbytes/cowcraft-plugins
LABEL maintainer="contact@beefbytes.com"

COPY common .

USER root
RUN chown -R mc:mc /home/mc \
    && chmod -R 774 /home/mc
USER mc
RUN /home/mc/server/scripts/on-build.sh