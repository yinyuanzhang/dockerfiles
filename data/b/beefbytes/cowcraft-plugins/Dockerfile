FROM beefbytes/cowcraft-base
LABEL maintainer="contact@beefbytes.com"

COPY common /home/mc/server/

USER root
RUN chown -R mc:mc /home/mc  \
    && chmod -R 774 /home/mc 
USER mc
