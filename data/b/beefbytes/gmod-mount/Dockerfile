FROM beefbytes/gmod-base
LABEL maintainer="contact@beefbytes.com"

WORKDIR /home/steam/steamcmd/

COPY common/tf2.sh tf2.sh
RUN ["bash", "tf2.sh"]

COPY common/css.sh css.sh
RUN ["bash", "css.sh"]
