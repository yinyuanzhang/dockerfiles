FROM debian:jessie
RUN apt-get update && apt-get install -y --no-install-recommends \
    default-jre \
    unzip \
    curl

ENV STARMADE_VERSION 20150907_154125
RUN curl -fL http://files.star-made.org/build/starmade-build_${STARMADE_VERSION}.zip  > /starmade.zip
RUN mkdir /STARMADE && unzip starmade.zip -d /STARMADE 


EXPOSE 4242
ADD execstarmade.sh /execstarmade.sh
RUN chmod +x /execstarmade.sh

CMD /execstarmade.sh

