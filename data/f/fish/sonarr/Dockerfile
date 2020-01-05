FROM mono:5.18

ENV VERSION=3.0.1.392
ENV URL=https://download.sonarr.tv/v3/phantom-develop/${VERSION}/Sonarr.phantom-develop.${VERSION}.linux.tar.gz

RUN apt-get -qy update && apt-get -qy install curl libmediainfo0v5 \
  && curl -Lsf "$URL" | tar -C /opt -xzf -

RUN useradd user && install -d -o user -g user /data
USER user
VOLUME /data

EXPOSE 8989
ENTRYPOINT [ "mono", "/opt/Sonarr/Sonarr.exe", "--data=/data/" ]
