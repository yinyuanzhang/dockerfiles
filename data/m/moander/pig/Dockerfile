FROM moander/bigtop:1.2.1

RUN apt-get update \
 && apt-get install -y --no-install-recommends pig \
 && rm -rf /var/lib/apt/lists/* \
 && mkdir /data

WORKDIR /data

VOLUME /data


